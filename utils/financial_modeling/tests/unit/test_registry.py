"""
Unit tests for the Variable Registry.

Tests:
- Loading YAML configurations
- Dependency resolution (topological sort)
- Circular dependency detection
- Variable lookup and filtering
"""

import pytest
from pathlib import Path
import tempfile
import yaml

# Import from parent directory
import sys
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from variable_engine.registry import VariableRegistry, Variable


class TestVariable:
    """Tests for the Variable dataclass."""

    def test_variable_creation_triangular(self):
        """Test creating a triangular distribution variable."""
        var = Variable(
            id="Test_Var",
            name="Test Variable",
            description="A test variable",
            unit="days",
            distribution="triangular",
            category="financial",
            params={"min": 10, "mode": 20, "max": 30}
        )

        assert var.id == "Test_Var"
        assert var.distribution == "triangular"
        assert var.params["mode"] == 20

    def test_variable_creation_beta(self):
        """Test creating a beta distribution variable."""
        var = Variable(
            id="Beta_Var",
            name="Beta Variable",
            description="A beta distribution",
            unit="fraction",
            distribution="beta",
            category="financial",
            params={"alpha": 2, "beta": 5, "min": 0, "max": 1}
        )

        assert var.distribution == "beta"
        assert var.params["alpha"] == 2

    def test_variable_missing_params_raises(self):
        """Test that missing required params raises ValueError."""
        with pytest.raises(ValueError, match="missing required params"):
            Variable(
                id="Bad_Var",
                name="Bad Variable",
                description="Missing params",
                unit="days",
                distribution="triangular",
                category="financial",
                params={"min": 10}  # Missing mode and max
            )

    def test_variable_fixed_distribution(self):
        """Test creating a fixed (deterministic) variable."""
        var = Variable(
            id="Fixed_Var",
            name="Fixed Variable",
            description="A constant",
            unit="$",
            distribution="fixed",
            category="financial",
            params={"value": 100}
        )

        assert var.distribution == "fixed"
        assert var.params["value"] == 100


class TestVariableRegistry:
    """Tests for the VariableRegistry class."""

    @pytest.fixture
    def temp_config_dir(self):
        """Create a temporary config directory with test YAML files."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_dir = Path(tmpdir) / "config"
            variables_dir = config_dir / "variables"
            variables_dir.mkdir(parents=True)

            # Create a test financial.yaml
            financial_yaml = {
                "category": "financial",
                "variables": [
                    {
                        "id": "Season_Extension_Days",
                        "name": "Season Extension Days",
                        "description": "Extra treatment days",
                        "unit": "days",
                        "distribution": "triangular",
                        "params": {"min": 14, "mode": 21, "max": 35}
                    },
                    {
                        "id": "Extension_Value",
                        "name": "Extension Value",
                        "description": "Value per extra day",
                        "unit": "$/day",
                        "distribution": "triangular",
                        "params": {"min": 3000, "mode": 7500, "max": 15000},
                        "drivers": ["Season_Extension_Days"]  # Depends on extension days
                    }
                ]
            }

            with open(variables_dir / "financial.yaml", "w") as f:
                yaml.dump(financial_yaml, f)

            yield config_dir

    def test_load_config(self, temp_config_dir):
        """Test loading configuration from YAML files."""
        registry = VariableRegistry(temp_config_dir)
        registry.load_config()

        assert len(registry) == 2
        assert "Season_Extension_Days" in registry
        assert "Extension_Value" in registry

    def test_get_variable(self, temp_config_dir):
        """Test retrieving a specific variable."""
        registry = VariableRegistry(temp_config_dir)
        registry.load_config()

        var = registry.get("Season_Extension_Days")
        assert var.id == "Season_Extension_Days"
        assert var.distribution == "triangular"
        assert var.params["mode"] == 21

    def test_get_nonexistent_raises(self, temp_config_dir):
        """Test that getting nonexistent variable raises KeyError."""
        registry = VariableRegistry(temp_config_dir)
        registry.load_config()

        with pytest.raises(KeyError, match="not found"):
            registry.get("Nonexistent_Variable")

    def test_dependency_order(self, temp_config_dir):
        """Test that variables are returned in dependency order."""
        registry = VariableRegistry(temp_config_dir)
        registry.load_config()

        ordered = registry.get_ordered()

        # Season_Extension_Days should come before Extension_Value
        # (since Extension_Value depends on it)
        ids = [v.id for v in ordered]
        assert ids.index("Season_Extension_Days") < ids.index("Extension_Value")

    def test_get_by_category(self, temp_config_dir):
        """Test filtering variables by category."""
        registry = VariableRegistry(temp_config_dir)
        registry.load_config()

        financial_vars = registry.get_by_category("financial")
        assert len(financial_vars) == 2

        # Non-existent category returns empty list
        empty = registry.get_by_category("nonexistent")
        assert len(empty) == 0

    def test_get_drivers(self, temp_config_dir):
        """Test getting driver (dependency) variables."""
        registry = VariableRegistry(temp_config_dir)
        registry.load_config()

        drivers = registry.get_drivers("Extension_Value")
        assert len(drivers) == 1
        assert drivers[0].id == "Season_Extension_Days"

    def test_get_dependents(self, temp_config_dir):
        """Test getting dependent variables."""
        registry = VariableRegistry(temp_config_dir)
        registry.load_config()

        dependents = registry.get_dependents("Season_Extension_Days")
        assert len(dependents) == 1
        assert dependents[0].id == "Extension_Value"


class TestCircularDependencies:
    """Tests for circular dependency detection."""

    @pytest.fixture
    def circular_config_dir(self):
        """Create config with circular dependencies."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_dir = Path(tmpdir) / "config"
            variables_dir = config_dir / "variables"
            variables_dir.mkdir(parents=True)

            # Create circular dependency: A -> B -> C -> A
            circular_yaml = {
                "category": "test",
                "variables": [
                    {
                        "id": "Var_A",
                        "name": "Variable A",
                        "description": "Depends on C",
                        "unit": "x",
                        "distribution": "fixed",
                        "params": {"value": 1},
                        "drivers": ["Var_C"]
                    },
                    {
                        "id": "Var_B",
                        "name": "Variable B",
                        "description": "Depends on A",
                        "unit": "x",
                        "distribution": "fixed",
                        "params": {"value": 2},
                        "drivers": ["Var_A"]
                    },
                    {
                        "id": "Var_C",
                        "name": "Variable C",
                        "description": "Depends on B",
                        "unit": "x",
                        "distribution": "fixed",
                        "params": {"value": 3},
                        "drivers": ["Var_B"]
                    }
                ]
            }

            with open(variables_dir / "circular.yaml", "w") as f:
                yaml.dump(circular_yaml, f)

            yield config_dir

    def test_circular_dependency_detected(self, circular_config_dir):
        """Test that circular dependencies raise ValueError."""
        registry = VariableRegistry(circular_config_dir)

        with pytest.raises(ValueError, match="Circular dependencies"):
            registry.load_config()


class TestLoadActualConfig:
    """Tests that load the actual config files."""

    @pytest.fixture
    def actual_config_dir(self):
        """Return path to actual config directory."""
        return Path(__file__).parent.parent.parent / "config"

    @pytest.mark.integration
    def test_load_financial_yaml(self, actual_config_dir):
        """Test loading the actual financial.yaml file."""
        if not (actual_config_dir / "variables" / "financial.yaml").exists():
            pytest.skip("financial.yaml not found")

        registry = VariableRegistry(actual_config_dir)
        registry.load_config()

        # Should have the 5 migrated financial variables
        assert len(registry) >= 5
        assert "Season_Extension_Days" in registry
        assert "Efficiency_Gain" in registry

    @pytest.mark.integration
    def test_financial_variables_have_correct_distributions(self, actual_config_dir):
        """Test that migrated variables have correct distribution types."""
        if not (actual_config_dir / "variables" / "financial.yaml").exists():
            pytest.skip("financial.yaml not found")

        registry = VariableRegistry(actual_config_dir)
        registry.load_config()

        # Triangular variables
        for var_id in ["Season_Extension_Days", "Extension_Value_Per_Day",
                       "Interventions_Avoided", "Treatment_Rate_Factor"]:
            if var_id in registry:
                var = registry.get(var_id)
                assert var.distribution == "triangular", f"{var_id} should be triangular"

        # Beta variable
        if "Efficiency_Gain" in registry:
            var = registry.get("Efficiency_Gain")
            assert var.distribution == "beta", "Efficiency_Gain should be beta"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
