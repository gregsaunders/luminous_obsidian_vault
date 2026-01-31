"""
Pytest configuration and shared fixtures for Luminous Wetland Monte Carlo tests.
"""
import os
import sys
import pytest
from pathlib import Path

# Add parent directory to path for imports
FINANCIAL_MODELING_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(FINANCIAL_MODELING_DIR))


@pytest.fixture
def financial_modeling_dir():
    """Return path to financial_modeling directory."""
    return FINANCIAL_MODELING_DIR


@pytest.fixture
def fixtures_dir():
    """Return path to fixtures directory."""
    return FINANCIAL_MODELING_DIR / "fixtures"


@pytest.fixture
def baseline_workbook_path(fixtures_dir):
    """Return path to baseline workbook for comparison."""
    return fixtures_dir / "baseline_workbook.xlsx"


@pytest.fixture
def generated_workbook_path(financial_modeling_dir):
    """Return path to generated workbook."""
    return financial_modeling_dir / "luminous_wetland_monte_carlo_model.xlsx"


@pytest.fixture
def content_sheets_dir(financial_modeling_dir):
    """Return path to content/sheets directory."""
    return financial_modeling_dir / "content" / "sheets"


# Test markers
def pytest_configure(config):
    """Configure custom pytest markers."""
    config.addinivalue_line(
        "markers", "unit: Unit tests (fast, no file I/O)"
    )
    config.addinivalue_line(
        "markers", "integration: Integration tests (generates workbook)"
    )
    config.addinivalue_line(
        "markers", "excel_live: Requires Excel/xlwings (slow, Mac/Windows only)"
    )
