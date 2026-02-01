"""
Config Validators - Validates YAML configuration files for the variable engine.

Provides schema validation for:
- Variable definitions
- Site configurations
- Model settings
"""

from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Any, Optional, Set
import yaml


class ValidationError(Exception):
    """Raised when configuration validation fails."""

    def __init__(self, message: str, errors: Optional[List[str]] = None):
        self.message = message
        self.errors = errors or []
        super().__init__(self._format_message())

    def _format_message(self) -> str:
        if not self.errors:
            return self.message
        error_list = "\n  - ".join(self.errors)
        return f"{self.message}\n  - {error_list}"


@dataclass
class SchemaField:
    """Defines a field in a configuration schema."""
    name: str
    required: bool = True
    field_type: type = str
    allowed_values: Optional[List[Any]] = None
    min_value: Optional[float] = None
    max_value: Optional[float] = None


class ConfigValidator:
    """
    Validates YAML configuration files against defined schemas.

    Usage:
        validator = ConfigValidator()
        errors = validator.validate_variable_file('/path/to/financial.yaml')
        if errors:
            raise ValidationError("Invalid config", errors)
    """

    # Required fields for variable definitions
    VARIABLE_REQUIRED_FIELDS = ['id', 'name', 'distribution']

    # Valid distribution types
    VALID_DISTRIBUTIONS = [
        'triangular', 'beta', 'normal', 'lognormal',
        'fixed', 'uniform', 'timeseries'
    ]

    # Required parameters per distribution
    DISTRIBUTION_PARAMS = {
        'triangular': ['min', 'mode', 'max'],
        'beta': ['alpha', 'beta', 'min', 'max'],
        'normal': ['mean', 'std'],
        'lognormal': ['mu', 'sigma'],
        'fixed': ['value'],
        'uniform': ['min', 'max'],
        'timeseries': ['values'],
    }

    # Valid categories
    VALID_CATEGORIES = ['environmental', 'ionic', 'kinetic', 'financial',
                        'timing', 'site', 'costs', 'kinetics_baseline']

    def validate_variable_file(self, file_path: Path) -> List[str]:
        """
        Validate a variable configuration YAML file.

        Args:
            file_path: Path to the YAML file

        Returns:
            List of validation error messages (empty if valid)
        """
        errors = []

        try:
            with open(file_path, 'r') as f:
                data = yaml.safe_load(f)
        except yaml.YAMLError as e:
            return [f"YAML parse error: {e}"]
        except FileNotFoundError:
            return [f"File not found: {file_path}"]

        if not data:
            return ["Empty configuration file"]

        # Validate top-level structure
        if 'variables' not in data:
            errors.append("Missing 'variables' key at top level")
            return errors

        if not isinstance(data['variables'], list):
            errors.append("'variables' must be a list")
            return errors

        # Validate category if present
        if 'category' in data:
            if data['category'] not in self.VALID_CATEGORIES:
                errors.append(
                    f"Invalid category '{data['category']}'. "
                    f"Must be one of: {self.VALID_CATEGORIES}"
                )

        # Validate each variable
        seen_ids: Set[str] = set()
        for i, var in enumerate(data['variables']):
            var_errors = self._validate_variable(var, i, seen_ids)
            errors.extend(var_errors)

        return errors

    def _validate_variable(
        self,
        var: Dict[str, Any],
        index: int,
        seen_ids: Set[str]
    ) -> List[str]:
        """Validate a single variable definition."""
        errors = []
        prefix = f"Variable [{index}]"

        if not isinstance(var, dict):
            return [f"{prefix}: Must be a dictionary"]

        # Check required fields
        for field in self.VARIABLE_REQUIRED_FIELDS:
            if field not in var:
                errors.append(f"{prefix}: Missing required field '{field}'")

        if 'id' in var:
            var_id = var['id']
            prefix = f"Variable '{var_id}'"

            # Check for duplicate IDs
            if var_id in seen_ids:
                errors.append(f"{prefix}: Duplicate variable ID")
            seen_ids.add(var_id)

            # Validate ID format (alphanumeric + underscore)
            if not var_id.replace('_', '').isalnum():
                errors.append(
                    f"{prefix}: ID must be alphanumeric with underscores only"
                )

        # Validate distribution
        if 'distribution' in var:
            dist = var['distribution']
            if dist not in self.VALID_DISTRIBUTIONS:
                errors.append(
                    f"{prefix}: Invalid distribution '{dist}'. "
                    f"Must be one of: {self.VALID_DISTRIBUTIONS}"
                )
            else:
                # Validate distribution parameters
                param_errors = self._validate_distribution_params(var, prefix)
                errors.extend(param_errors)

        # Validate drivers (must be list of strings)
        if 'drivers' in var:
            if not isinstance(var['drivers'], list):
                errors.append(f"{prefix}: 'drivers' must be a list")
            else:
                for driver in var['drivers']:
                    if not isinstance(driver, str):
                        errors.append(f"{prefix}: Driver values must be strings")

        # Validate unit (should be string)
        if 'unit' in var and not isinstance(var['unit'], str):
            errors.append(f"{prefix}: 'unit' must be a string")

        return errors

    def _validate_distribution_params(
        self,
        var: Dict[str, Any],
        prefix: str
    ) -> List[str]:
        """Validate distribution-specific parameters."""
        errors = []
        dist = var.get('distribution')
        params = var.get('params', {})

        if dist not in self.DISTRIBUTION_PARAMS:
            return errors  # Unknown distribution handled elsewhere

        required_params = self.DISTRIBUTION_PARAMS[dist]
        for param in required_params:
            if param not in params:
                errors.append(
                    f"{prefix}: Missing required parameter '{param}' "
                    f"for {dist} distribution"
                )

        # Validate numeric parameters
        numeric_params = ['min', 'max', 'mode', 'mean', 'std', 'alpha', 'beta', 'mu', 'sigma', 'value']
        for param in numeric_params:
            if param in params:
                val = params[param]
                if not isinstance(val, (int, float, str)):
                    errors.append(
                        f"{prefix}: Parameter '{param}' must be numeric or a reference"
                    )

        # Validate parameter relationships
        if dist == 'triangular' and all(p in params for p in ['min', 'mode', 'max']):
            min_v, mode_v, max_v = params['min'], params['mode'], params['max']
            if all(isinstance(v, (int, float)) for v in [min_v, mode_v, max_v]):
                if not (min_v <= mode_v <= max_v):
                    errors.append(
                        f"{prefix}: Triangular requires min <= mode <= max"
                    )

        if dist == 'beta' and all(p in params for p in ['alpha', 'beta']):
            alpha, beta = params['alpha'], params['beta']
            if isinstance(alpha, (int, float)) and alpha <= 0:
                errors.append(f"{prefix}: Beta alpha must be > 0")
            if isinstance(beta, (int, float)) and beta <= 0:
                errors.append(f"{prefix}: Beta beta must be > 0")

        if dist == 'normal' and 'std' in params:
            std = params['std']
            if isinstance(std, (int, float)) and std < 0:
                errors.append(f"{prefix}: Normal std must be >= 0")

        return errors

    def validate_site_file(self, file_path: Path) -> List[str]:
        """
        Validate a site configuration YAML file.

        Args:
            file_path: Path to the YAML file

        Returns:
            List of validation error messages
        """
        errors = []

        try:
            with open(file_path, 'r') as f:
                data = yaml.safe_load(f)
        except yaml.YAMLError as e:
            return [f"YAML parse error: {e}"]
        except FileNotFoundError:
            return [f"File not found: {file_path}"]

        if not data:
            return ["Empty configuration file"]

        # Required fields for site config
        required = ['site_id', 'name']
        for field in required:
            if field not in data:
                errors.append(f"Missing required field '{field}'")

        # Validate kinetics section if present
        if 'kinetics' in data:
            kinetics = data['kinetics']
            if not isinstance(kinetics, dict):
                errors.append("'kinetics' must be a dictionary")
            else:
                # Validate kinetics parameters
                for key, value in kinetics.items():
                    if not isinstance(value, (int, float)):
                        errors.append(f"Kinetics parameter '{key}' must be numeric")

        return errors

    def validate_model_file(self, file_path: Path) -> List[str]:
        """
        Validate the model configuration YAML file.

        Args:
            file_path: Path to model.yaml

        Returns:
            List of validation error messages
        """
        errors = []

        try:
            with open(file_path, 'r') as f:
                data = yaml.safe_load(f)
        except yaml.YAMLError as e:
            return [f"YAML parse error: {e}"]
        except FileNotFoundError:
            return [f"File not found: {file_path}"]

        if not data:
            return ["Empty configuration file"]

        # Validate simulation settings
        if 'simulation' in data:
            sim = data['simulation']
            if 'iterations' in sim:
                iterations = sim['iterations']
                if not isinstance(iterations, int) or iterations < 1:
                    errors.append("simulation.iterations must be a positive integer")
                if iterations > 10000:
                    errors.append("simulation.iterations should not exceed 10000")

        return errors

    def validate_all(self, config_dir: Path) -> Dict[str, List[str]]:
        """
        Validate all configuration files in a directory.

        Args:
            config_dir: Path to config directory

        Returns:
            Dictionary mapping file paths to their validation errors
        """
        all_errors = {}

        # Validate variable files
        variables_dir = config_dir / "variables"
        if variables_dir.exists():
            for yaml_file in variables_dir.glob("*.yaml"):
                errors = self.validate_variable_file(yaml_file)
                if errors:
                    all_errors[str(yaml_file)] = errors

        # Validate site files
        sites_dir = config_dir / "sites"
        if sites_dir.exists():
            for yaml_file in sites_dir.glob("*.yaml"):
                errors = self.validate_site_file(yaml_file)
                if errors:
                    all_errors[str(yaml_file)] = errors

        # Validate model file
        model_file = config_dir / "model.yaml"
        if model_file.exists():
            errors = self.validate_model_file(model_file)
            if errors:
                all_errors[str(model_file)] = errors

        return all_errors
