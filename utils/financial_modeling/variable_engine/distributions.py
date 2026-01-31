"""
Distribution Formulas - Generates Excel formulas for stochastic distributions.

Provides Excel-native formulas for:
- Triangular distribution (inverse transform method)
- Beta distribution (using BETA.INV)
- Normal distribution (using NORM.INV)
- Lognormal distribution (using LOGNORM.INV)
- Fixed values
- Time series (monthly profiles)

All formulas use RAND() for random number generation, making them
compatible with Excel's Data Table for Monte Carlo simulation.
"""

from typing import Dict, Any, Optional, Union


class DistributionFormulas:
    """
    Generates Excel formulas for various probability distributions.

    All formulas produce random draws that can be recalculated by Excel
    to perform Monte Carlo simulation via Data Tables.

    Usage:
        formula = DistributionFormulas.triangular(min_val=14, mode_val=21, max_val=35)
        # Returns Excel formula string
    """

    @staticmethod
    def triangular(
        min_val: Union[float, str],
        mode_val: Union[float, str],
        max_val: Union[float, str],
        rand_cell: str = "RAND()"
    ) -> str:
        """
        Generate Excel formula for triangular distribution using inverse transform.

        The triangular distribution is defined by min, mode, and max values.
        This uses the inverse CDF method for exact sampling.

        Args:
            min_val: Minimum value (number or Excel reference)
            mode_val: Mode/peak value (number or Excel reference)
            max_val: Maximum value (number or Excel reference)
            rand_cell: Random number source (default: RAND())

        Returns:
            Excel formula string (without leading =)

        Example:
            >>> DistributionFormulas.triangular(14, 21, 35)
            'IF(RAND()<(21-14)/(35-14), 14+SQRT(RAND()*(35-14)*(21-14)), 35-SQRT((1-RAND())*(35-14)*(35-21)))'
        """
        # For proper inverse transform, we need consistent RAND() usage
        # Using nested IF with separate RAND() calls for each branch
        return (
            f"IF({rand_cell}<({mode_val}-{min_val})/({max_val}-{min_val}),"
            f"{min_val}+SQRT({rand_cell}*({max_val}-{min_val})*({mode_val}-{min_val})),"
            f"{max_val}-SQRT((1-{rand_cell})*({max_val}-{min_val})*({max_val}-{mode_val})))"
        )

    @staticmethod
    def triangular_named(
        min_name: str,
        mode_name: str,
        max_name: str,
        rand_cell: str = "RAND()"
    ) -> str:
        """
        Generate triangular distribution formula using named ranges.

        Args:
            min_name: Named range for minimum value
            mode_name: Named range for mode value
            max_name: Named range for maximum value
            rand_cell: Random number source

        Returns:
            Excel formula using named ranges
        """
        return DistributionFormulas.triangular(
            min_val=min_name,
            mode_val=mode_name,
            max_val=max_name,
            rand_cell=rand_cell
        )

    @staticmethod
    def beta(
        alpha: Union[float, str],
        beta: Union[float, str],
        min_val: Union[float, str] = 0,
        max_val: Union[float, str] = 1,
        rand_cell: str = "RAND()"
    ) -> str:
        """
        Generate Excel formula for scaled Beta distribution.

        Uses BETA.INV for the standard Beta(alpha, beta) on [0,1],
        then scales to [min_val, max_val].

        Args:
            alpha: Alpha shape parameter (> 0)
            beta: Beta shape parameter (> 0)
            min_val: Minimum of scaled range (default: 0)
            max_val: Maximum of scaled range (default: 1)
            rand_cell: Random number source

        Returns:
            Excel formula string

        Example:
            >>> DistributionFormulas.beta(2, 5, 0.05, 0.30)
            '0.05+(0.30-0.05)*BETA.INV(RAND(),2,5)'
        """
        return f"{min_val}+({max_val}-{min_val})*BETA.INV({rand_cell},{alpha},{beta})"

    @staticmethod
    def beta_named(
        alpha_name: str,
        beta_name: str,
        min_name: str,
        max_name: str,
        rand_cell: str = "RAND()"
    ) -> str:
        """Generate Beta distribution formula using named ranges."""
        return DistributionFormulas.beta(
            alpha=alpha_name,
            beta=beta_name,
            min_val=min_name,
            max_val=max_name,
            rand_cell=rand_cell
        )

    @staticmethod
    def normal(
        mean: Union[float, str],
        std: Union[float, str],
        rand_cell: str = "RAND()"
    ) -> str:
        """
        Generate Excel formula for Normal distribution.

        Uses NORM.INV to convert uniform random to normal.

        Args:
            mean: Mean of the distribution
            std: Standard deviation
            rand_cell: Random number source

        Returns:
            Excel formula string

        Example:
            >>> DistributionFormulas.normal(100, 15)
            'NORM.INV(RAND(),100,15)'
        """
        return f"NORM.INV({rand_cell},{mean},{std})"

    @staticmethod
    def lognormal(
        mu: Union[float, str],
        sigma: Union[float, str],
        rand_cell: str = "RAND()"
    ) -> str:
        """
        Generate Excel formula for Lognormal distribution.

        Uses LOGNORM.INV where mu and sigma are parameters of the
        underlying normal distribution (not the mean/std of the lognormal).

        Args:
            mu: Mean of underlying normal distribution
            sigma: Std dev of underlying normal distribution
            rand_cell: Random number source

        Returns:
            Excel formula string

        Example:
            >>> DistributionFormulas.lognormal(2.5, 0.3)
            'LOGNORM.INV(RAND(),2.5,0.3)'
        """
        return f"LOGNORM.INV({rand_cell},{mu},{sigma})"

    @staticmethod
    def fixed(value: Union[float, str]) -> str:
        """
        Generate Excel formula for a fixed (deterministic) value.

        Args:
            value: The fixed value or cell reference

        Returns:
            Excel formula string (just the value/reference)
        """
        return str(value)

    @staticmethod
    def uniform(
        min_val: Union[float, str],
        max_val: Union[float, str],
        rand_cell: str = "RAND()"
    ) -> str:
        """
        Generate Excel formula for Uniform distribution.

        Args:
            min_val: Minimum value
            max_val: Maximum value
            rand_cell: Random number source

        Returns:
            Excel formula string

        Example:
            >>> DistributionFormulas.uniform(10, 50)
            '10+(50-10)*RAND()'
        """
        return f"{min_val}+({max_val}-{min_val})*{rand_cell}"

    @staticmethod
    def q10_factor(
        temp_cell: str,
        reference_temp: Union[float, str] = 20,
        q10_value: Union[float, str] = 2
    ) -> str:
        """
        Generate Excel formula for Q10 temperature coefficient.

        Q10 describes how reaction rates change with temperature.
        Q10 = 2 means rate doubles for every 10°C increase.

        Formula: Q10^((T - T_ref) / 10)

        Args:
            temp_cell: Cell reference for temperature value
            reference_temp: Reference temperature (default: 20°C)
            q10_value: Q10 coefficient (default: 2)

        Returns:
            Excel formula string

        Example:
            >>> DistributionFormulas.q10_factor("Stoch_Temp", 20, 2)
            '2^((Stoch_Temp-20)/10)'
        """
        return f"{q10_value}^(({temp_cell}-{reference_temp})/10)"

    @staticmethod
    def bounded_modifier(
        value_cell: str,
        threshold: Union[float, str],
        direction: str = "above"
    ) -> str:
        """
        Generate Excel formula for a bounded modifier (0 or 1).

        Returns 1 if the value is above/below the threshold, 0 otherwise.

        Args:
            value_cell: Cell reference for the value to test
            threshold: Threshold value
            direction: "above" or "below"

        Returns:
            Excel formula string

        Example:
            >>> DistributionFormulas.bounded_modifier("Stoch_DO", 6.5, "above")
            'IF(Stoch_DO>6.5,1,0)'
        """
        operator = ">" if direction == "above" else "<"
        return f"IF({value_cell}{operator}{threshold},1,0)"

    @staticmethod
    def linear_modifier(
        value_cell: str,
        threshold: Union[float, str],
        direction: str = "above"
    ) -> str:
        """
        Generate Excel formula for a linear modifier (0 to 1).

        Returns a value between 0 and 1 based on how the value
        compares to the threshold.

        Args:
            value_cell: Cell reference for the value
            threshold: Threshold value
            direction: "above" (value/threshold) or "below" (threshold/value)

        Returns:
            Excel formula string

        Example:
            >>> DistributionFormulas.linear_modifier("Stoch_DO", 6.5, "above")
            'IF(Stoch_DO>=6.5,1,Stoch_DO/6.5)'
        """
        if direction == "above":
            return f"IF({value_cell}>={threshold},1,{value_cell}/{threshold})"
        else:
            return f"IF({value_cell}<={threshold},1,{threshold}/{value_cell})"

    @classmethod
    def from_variable(cls, variable: 'Variable', rand_cell: str = "RAND()") -> str:
        """
        Generate Excel formula from a Variable object.

        Args:
            variable: Variable object with distribution and params
            rand_cell: Random number source

        Returns:
            Excel formula string

        Raises:
            ValueError: If distribution type is not supported
        """
        dist = variable.distribution
        params = variable.params

        if dist == 'triangular':
            return cls.triangular(
                min_val=params['min'],
                mode_val=params['mode'],
                max_val=params['max'],
                rand_cell=rand_cell
            )
        elif dist == 'beta':
            return cls.beta(
                alpha=params['alpha'],
                beta=params['beta'],
                min_val=params.get('min', 0),
                max_val=params.get('max', 1),
                rand_cell=rand_cell
            )
        elif dist == 'normal':
            return cls.normal(
                mean=params['mean'],
                std=params['std'],
                rand_cell=rand_cell
            )
        elif dist == 'lognormal':
            return cls.lognormal(
                mu=params['mu'],
                sigma=params['sigma'],
                rand_cell=rand_cell
            )
        elif dist == 'fixed':
            return cls.fixed(params['value'])
        elif dist == 'uniform':
            return cls.uniform(
                min_val=params['min'],
                max_val=params['max'],
                rand_cell=rand_cell
            )
        else:
            raise ValueError(f"Unsupported distribution type: {dist}")
