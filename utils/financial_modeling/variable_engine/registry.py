"""
Variable Registry - Loads and manages stochastic variables from YAML configuration.

Provides:
- YAML-based variable definitions with distribution parameters
- Dependency resolution via topological sort
- Named range generation for Excel formulas
"""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Any, Set
import yaml


@dataclass
class Variable:
    """Represents a stochastic or deterministic variable in the model."""

    id: str
    name: str
    description: str
    unit: str
    distribution: str  # 'triangular', 'beta', 'normal', 'lognormal', 'fixed', 'timeseries'
    category: str  # 'environmental', 'ionic', 'kinetic', 'financial'

    # Distribution parameters (varies by distribution type)
    params: Dict[str, Any] = field(default_factory=dict)

    # Dependencies - other variables this one depends on
    drivers: List[str] = field(default_factory=list)

    # Excel named range (set during workbook generation)
    excel_range: Optional[str] = None

    # Sheet where this variable is defined
    sheet: Optional[str] = None

    # Whether this is a user-editable input
    is_input: bool = True

    def __post_init__(self):
        """Validate distribution parameters."""
        required_params = self._get_required_params()
        missing = set(required_params) - set(self.params.keys())
        if missing:
            raise ValueError(
                f"Variable '{self.id}' missing required params for {self.distribution}: {missing}"
            )

    def _get_required_params(self) -> List[str]:
        """Return required parameters for this distribution type."""
        requirements = {
            'triangular': ['min', 'mode', 'max'],
            'beta': ['alpha', 'beta', 'min', 'max'],
            'normal': ['mean', 'std'],
            'lognormal': ['mu', 'sigma'],
            'fixed': ['value'],
            'timeseries': ['values'],  # Monthly values
        }
        return requirements.get(self.distribution, [])


class VariableRegistry:
    """
    Manages all model variables loaded from YAML configuration files.

    Usage:
        registry = VariableRegistry()
        registry.load_config('/path/to/config/variables')

        # Get a specific variable
        temp = registry.get('Temp_Water')

        # Get all variables in dependency order
        for var in registry.get_ordered():
            print(var.id)
    """

    def __init__(self, config_dir: Optional[Path] = None):
        """
        Initialize the registry.

        Args:
            config_dir: Path to config directory. If None, uses default location.
        """
        self._variables: Dict[str, Variable] = {}
        self._categories: Dict[str, List[str]] = {}
        self._dependency_order: Optional[List[str]] = None

        if config_dir is None:
            self.config_dir = Path(__file__).parent.parent / "config"
        else:
            self.config_dir = Path(config_dir)

    def load_config(self, variables_dir: Optional[Path] = None) -> None:
        """
        Load all variable definitions from YAML files.

        Args:
            variables_dir: Path to variables config directory.
                          If None, uses config_dir/variables.
        """
        if variables_dir is None:
            variables_dir = self.config_dir / "variables"

        if not variables_dir.exists():
            raise FileNotFoundError(f"Variables config directory not found: {variables_dir}")

        # Load all YAML files in the variables directory
        for yaml_file in variables_dir.glob("*.yaml"):
            self._load_yaml_file(yaml_file)

        # Resolve dependencies and compute order
        self._resolve_dependencies()

    def _load_yaml_file(self, file_path: Path) -> None:
        """Load variables from a single YAML file."""
        with open(file_path, 'r') as f:
            data = yaml.safe_load(f)

        if not data or 'variables' not in data:
            return

        category = data.get('category', file_path.stem)

        for var_data in data['variables']:
            var = Variable(
                id=var_data['id'],
                name=var_data.get('name', var_data['id']),
                description=var_data.get('description', ''),
                unit=var_data.get('unit', ''),
                distribution=var_data.get('distribution', 'fixed'),
                category=category,
                params=var_data.get('params', {}),
                drivers=var_data.get('drivers', []),
                sheet=var_data.get('sheet'),
                is_input=var_data.get('is_input', True),
            )

            self._variables[var.id] = var

            # Track by category
            if category not in self._categories:
                self._categories[category] = []
            self._categories[category].append(var.id)

    def _resolve_dependencies(self) -> None:
        """
        Resolve variable dependencies using topological sort.

        Raises:
            ValueError: If circular dependencies are detected.
        """
        # Build adjacency list
        graph: Dict[str, Set[str]] = {var_id: set() for var_id in self._variables}

        for var_id, var in self._variables.items():
            for driver in var.drivers:
                if driver in self._variables:
                    graph[var_id].add(driver)

        # Kahn's algorithm for topological sort
        in_degree = {var_id: 0 for var_id in self._variables}
        for var_id, deps in graph.items():
            for dep in deps:
                in_degree[var_id] += 1

        # Start with variables that have no dependencies
        queue = [var_id for var_id, degree in in_degree.items() if degree == 0]
        result = []

        while queue:
            var_id = queue.pop(0)
            result.append(var_id)

            # Find all variables that depend on this one
            for other_id, deps in graph.items():
                if var_id in deps:
                    in_degree[other_id] -= 1
                    if in_degree[other_id] == 0:
                        queue.append(other_id)

        # Check for circular dependencies
        if len(result) != len(self._variables):
            remaining = set(self._variables.keys()) - set(result)
            raise ValueError(f"Circular dependencies detected involving: {remaining}")

        self._dependency_order = result

    def get(self, var_id: str) -> Variable:
        """Get a variable by ID."""
        if var_id not in self._variables:
            raise KeyError(f"Variable '{var_id}' not found in registry")
        return self._variables[var_id]

    def get_all(self) -> Dict[str, Variable]:
        """Get all variables as a dictionary."""
        return self._variables.copy()

    def get_all_variable_ids(self) -> List[str]:
        """Get all variable IDs."""
        return list(self._variables.keys())

    def get_ordered(self) -> List[Variable]:
        """Get all variables in dependency order (dependencies first)."""
        if self._dependency_order is None:
            self._resolve_dependencies()
        return [self._variables[var_id] for var_id in self._dependency_order]

    def get_by_category(self, category: str) -> List[Variable]:
        """Get all variables in a specific category."""
        if category not in self._categories:
            return []
        return [self._variables[var_id] for var_id in self._categories[category]]

    def get_categories(self) -> List[str]:
        """Get all category names."""
        return list(self._categories.keys())

    def get_drivers(self, var_id: str) -> List[Variable]:
        """Get all variables that drive (are dependencies of) a given variable."""
        var = self.get(var_id)
        return [self._variables[d] for d in var.drivers if d in self._variables]

    def get_dependents(self, var_id: str) -> List[Variable]:
        """Get all variables that depend on a given variable."""
        result = []
        for other_id, other_var in self._variables.items():
            if var_id in other_var.drivers:
                result.append(other_var)
        return result

    def __len__(self) -> int:
        return len(self._variables)

    def __contains__(self, var_id: str) -> bool:
        return var_id in self._variables

    def __iter__(self):
        return iter(self._variables.values())
