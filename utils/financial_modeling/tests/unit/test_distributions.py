"""
Unit tests for Distribution Formula generators.

Tests Excel formula generation for:
- Triangular distribution (inverse transform method)
- Beta distribution (BETA.INV)
- Normal distribution (NORM.INV)
- Lognormal distribution (LOGNORM.INV)
- Q10 temperature coefficient
- Bounded and linear modifiers
"""

import pytest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from variable_engine.distributions import DistributionFormulas
from variable_engine.registry import Variable


class TestTriangularDistribution:
    """Tests for triangular distribution formula generation."""

    def test_triangular_with_numbers(self):
        """Test triangular formula with numeric values."""
        formula = DistributionFormulas.triangular(
            min_val=14, mode_val=21, max_val=35
        )

        # Should contain the three values
        assert "14" in formula
        assert "21" in formula
        assert "35" in formula

        # Should use SQRT for inverse transform
        assert "SQRT" in formula

        # Should use IF for conditional branch
        assert "IF" in formula

    def test_triangular_with_named_ranges(self):
        """Test triangular formula with Excel named ranges."""
        formula = DistributionFormulas.triangular_named(
            min_name="Tri_Test_Min",
            mode_name="Tri_Test_Mode",
            max_name="Tri_Test_Max"
        )

        assert "Tri_Test_Min" in formula
        assert "Tri_Test_Mode" in formula
        assert "Tri_Test_Max" in formula

    def test_triangular_custom_rand(self):
        """Test triangular with custom random cell reference."""
        formula = DistributionFormulas.triangular(
            min_val=10, mode_val=20, max_val=30,
            rand_cell="$K$1"
        )

        assert "$K$1" in formula
        assert "RAND()" not in formula


class TestBetaDistribution:
    """Tests for Beta distribution formula generation."""

    def test_beta_standard(self):
        """Test standard Beta distribution on [0,1]."""
        formula = DistributionFormulas.beta(
            alpha=2, beta=5, min_val=0, max_val=1
        )

        assert "BETA.INV" in formula
        assert "2" in formula  # alpha
        assert "5" in formula  # beta

    def test_beta_scaled(self):
        """Test scaled Beta distribution."""
        formula = DistributionFormulas.beta(
            alpha=2, beta=5, min_val=0.05, max_val=0.40
        )

        # Should scale the output
        assert "0.05" in formula
        assert "0.4" in formula  # Python may format as 0.4 not 0.40
        assert "BETA.INV" in formula

    def test_beta_named(self):
        """Test Beta formula with named ranges."""
        formula = DistributionFormulas.beta_named(
            alpha_name="Beta_Test_Alpha",
            beta_name="Beta_Test_Beta",
            min_name="Beta_Test_Min",
            max_name="Beta_Test_Max"
        )

        assert "Beta_Test_Alpha" in formula
        assert "Beta_Test_Beta" in formula


class TestNormalDistribution:
    """Tests for Normal distribution formula generation."""

    def test_normal_basic(self):
        """Test normal distribution formula."""
        formula = DistributionFormulas.normal(mean=100, std=15)

        assert "NORM.INV" in formula
        assert "100" in formula
        assert "15" in formula
        assert "RAND()" in formula

    def test_normal_with_references(self):
        """Test normal with cell references."""
        formula = DistributionFormulas.normal(
            mean="Mean_Value", std="StdDev_Value"
        )

        assert "Mean_Value" in formula
        assert "StdDev_Value" in formula


class TestLognormalDistribution:
    """Tests for Lognormal distribution formula generation."""

    def test_lognormal_basic(self):
        """Test lognormal distribution formula."""
        formula = DistributionFormulas.lognormal(mu=2.5, sigma=0.3)

        assert "LOGNORM.INV" in formula
        assert "2.5" in formula
        assert "0.3" in formula


class TestFixedAndUniform:
    """Tests for fixed and uniform distributions."""

    def test_fixed_numeric(self):
        """Test fixed value (constant)."""
        formula = DistributionFormulas.fixed(100)
        assert formula == "100"

    def test_fixed_reference(self):
        """Test fixed with cell reference."""
        formula = DistributionFormulas.fixed("Base_Value")
        assert formula == "Base_Value"

    def test_uniform_basic(self):
        """Test uniform distribution."""
        formula = DistributionFormulas.uniform(min_val=10, max_val=50)

        assert "10" in formula
        assert "50" in formula
        assert "RAND()" in formula


class TestQ10Factor:
    """Tests for Q10 temperature coefficient formula."""

    def test_q10_default(self):
        """Test Q10 with default parameters."""
        formula = DistributionFormulas.q10_factor(
            temp_cell="Stoch_Temp"
        )

        # Default Q10=2, reference=20
        assert "2^" in formula
        assert "Stoch_Temp" in formula
        assert "20" in formula
        assert "10" in formula

    def test_q10_custom_parameters(self):
        """Test Q10 with custom parameters."""
        formula = DistributionFormulas.q10_factor(
            temp_cell="Temp_Water",
            reference_temp=15,
            q10_value=2.5
        )

        assert "2.5^" in formula
        assert "15" in formula

    def test_q10_formula_correctness(self):
        """Verify Q10 formula structure is correct."""
        formula = DistributionFormulas.q10_factor("T", 20, 2)

        # Should be: 2^((T-20)/10)
        assert formula == "2^((T-20)/10)"


class TestModifiers:
    """Tests for modifier formula generation."""

    def test_bounded_modifier_above(self):
        """Test bounded modifier with 'above' direction."""
        formula = DistributionFormulas.bounded_modifier(
            value_cell="Stoch_DO",
            threshold=6.5,
            direction="above"
        )

        assert "IF" in formula
        assert "Stoch_DO" in formula
        assert "6.5" in formula
        assert ">" in formula

    def test_bounded_modifier_below(self):
        """Test bounded modifier with 'below' direction."""
        formula = DistributionFormulas.bounded_modifier(
            value_cell="Stoch_Turbidity",
            threshold=100,
            direction="below"
        )

        assert "<" in formula

    def test_linear_modifier_above(self):
        """Test linear modifier with 'above' direction."""
        formula = DistributionFormulas.linear_modifier(
            value_cell="Stoch_DO",
            threshold=6.5,
            direction="above"
        )

        # Should have IF for conditional
        assert "IF" in formula
        # Should divide value by threshold when below
        assert "/" in formula


class TestFromVariable:
    """Tests for generating formulas from Variable objects."""

    def test_from_variable_triangular(self):
        """Test formula generation from triangular Variable."""
        var = Variable(
            id="Test_Tri",
            name="Test Triangular",
            description="Test",
            unit="days",
            distribution="triangular",
            category="test",
            params={"min": 10, "mode": 20, "max": 30}
        )

        formula = DistributionFormulas.from_variable(var)

        assert "SQRT" in formula
        assert "10" in formula
        assert "20" in formula
        assert "30" in formula

    def test_from_variable_beta(self):
        """Test formula generation from beta Variable."""
        var = Variable(
            id="Test_Beta",
            name="Test Beta",
            description="Test",
            unit="fraction",
            distribution="beta",
            category="test",
            params={"alpha": 2, "beta": 5, "min": 0, "max": 1}
        )

        formula = DistributionFormulas.from_variable(var)

        assert "BETA.INV" in formula

    def test_from_variable_unsupported_raises(self):
        """Test that unsupported distribution raises ValueError."""
        var = Variable(
            id="Test_Bad",
            name="Test Bad",
            description="Test",
            unit="x",
            distribution="timeseries",  # Not fully supported in from_variable
            category="test",
            params={"values": [1, 2, 3]}
        )

        with pytest.raises(ValueError, match="Unsupported distribution"):
            DistributionFormulas.from_variable(var)


class TestScientificAccuracy:
    """Tests to verify scientific accuracy of formulas."""

    def test_q10_at_30c_equals_2(self):
        """Verify Q10=2 at T=30°C produces factor of 2.0."""
        # Q10 formula: 2^((T-20)/10)
        # At T=30: 2^((30-20)/10) = 2^1 = 2.0
        formula = DistributionFormulas.q10_factor("30", 20, 2)

        # Formula should evaluate to 2 when T=30
        # We can't evaluate Excel formulas here, but verify structure
        assert "2^((30-20)/10)" == formula

    def test_q10_at_10c_equals_half(self):
        """Verify Q10=2 at T=10°C produces factor of 0.5."""
        # At T=10: 2^((10-20)/10) = 2^(-1) = 0.5
        formula = DistributionFormulas.q10_factor("10", 20, 2)
        assert "2^((10-20)/10)" == formula


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
