"""
Variable Engine for Luminous Wetland Monte Carlo Model.

This module provides configuration-driven variable management for the financial model,
including:
- Variable registry with YAML-based definitions
- Distribution formula generators for Excel
- Dependency resolution and validation
"""

from .registry import VariableRegistry, Variable
from .distributions import DistributionFormulas
from .validators import ConfigValidator, ValidationError

__all__ = [
    'VariableRegistry',
    'Variable',
    'DistributionFormulas',
    'ConfigValidator',
    'ValidationError',
]
