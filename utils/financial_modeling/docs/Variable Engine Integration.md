# Variable Engine Integration

This document describes how the `variable_engine/` infrastructure integrates with `luminous_wetland_monte_carlo.py` to provide configuration-driven variable management for the financial model.

## Overview

The variable engine replaces hardcoded variable definitions with YAML configuration files, enabling:
- Centralized variable definitions with metadata
- Automatic distribution parameter generation
- Dynamic INPUT_REGISTRY generation
- Validation and dependency resolution

## Architecture

```
config/
├── model.yaml            # Simulation settings (iterations, discount rate, etc.)
├── variables/
│   ├── environmental.yaml    # Environmental drivers (Temp, UV, DO, etc.)
│   ├── ionic.yaml            # Ionic balance variables
│   ├── kinetic.yaml          # Kinetic rate modifiers
│   ├── financial.yaml        # Stochastic financial variables (triangular/beta)
│   ├── timing.yaml           # Seasonal timing parameters
│   ├── site.yaml             # Site configuration
│   ├── costs.yaml            # Cost parameters
│   └── kinetics_baseline.yaml # Baseline treatment kinetics
└── sites/
    └── kearl.yaml            # Site-specific parameters

variable_engine/
├── __init__.py           # Public API exports
├── registry.py           # VariableRegistry class
├── distributions.py      # DistributionFormulas class
└── validators.py         # ConfigValidator class
```

## Model Configuration (model.yaml)

The `config/model.yaml` file controls simulation-wide settings:

```yaml
simulation:
  iterations: 1000         # Monte Carlo iteration count
  random_seed: null        # Set integer for reproducibility

financial:
  discount_rate: 0.048     # 4.8% discount rate
  projection_years: 5
  base_year: 2026

output:
  include_percentiles: [10, 25, 50, 75, 90]
```

### Accessing Model Config

```python
config = get_model_config()
iterations = config['simulation']['iterations']  # 1000
```

The iteration count flows to:
- Sheet title: "Monte Carlo Simulation (1000 iterations)"
- Data Table row count
- Probability formulas: `=COUNTIF(...)/1000`

## YAML Configuration Format

### Basic Variable Structure

```yaml
category: timing  # Category name (must match VALID_CATEGORIES)

variables:
  - id: Season_Start_Month          # Unique identifier (alphanumeric + underscore)
    name: Season Start Month        # Human-readable name
    description: >-                 # Multi-line description
      Month when the treatment season begins.
    unit: month                     # Unit of measurement
    distribution: fixed             # Distribution type
    params:                         # Distribution-specific parameters
      value: 5
      notes: May                    # Optional notes (shown in spreadsheet)
    sheet: 4_Assumptions            # Target Excel sheet
    is_input: true                  # Whether user-editable
```

### Distribution Types

| Distribution | Required Params | Example |
|-------------|-----------------|---------|
| `fixed` | `value` | `params: { value: 100 }` |
| `triangular` | `min`, `mode`, `max` | `params: { min: 14, mode: 21, max: 35 }` |
| `beta` | `alpha`, `beta`, `min`, `max` | `params: { alpha: 2, beta: 5, min: 0.05, max: 0.40 }` |
| `normal` | `mean`, `std` | `params: { mean: 100, std: 15 }` |
| `lognormal` | `mu`, `sigma` | `params: { mu: 2.5, sigma: 0.3 }` |
| `uniform` | `min`, `max` | `params: { min: 10, max: 50 }` |
| `timeseries` | `values` (dict) | `params: { values: { may: 10, jun: 16 } }` |

### Valid Categories

Categories are defined in `validators.py`:

```python
VALID_CATEGORIES = [
    'environmental',      # Environmental drivers
    'ionic',              # Ionic balance
    'kinetic',            # Kinetic modifiers
    'financial',          # Stochastic financial variables
    'timing',             # Seasonal timing
    'site',               # Site configuration
    'costs',              # Cost parameters
    'kinetics_baseline'   # Baseline kinetics
]
```

## Python Integration

### Getting the Registry

```python
from variable_engine import VariableRegistry

# Module-level singleton (lazy initialization)
def get_registry() -> VariableRegistry:
    global _registry
    if _registry is None:
        _registry = VariableRegistry()
        _registry.load_config()  # Loads all config/variables/*.yaml
    return _registry
```

### Iterating by Category

```python
registry = get_registry()

# Get all timing variables
for var in registry.get_by_category('timing'):
    print(f"{var.id}: {var.params.get('value')}")

# Filter by distribution type
tri_vars = [v for v in registry.get_by_category('financial')
            if v.distribution == 'triangular']
```

### Generating Excel Formulas

```python
from variable_engine import DistributionFormulas

# Triangular with literal values
formula = DistributionFormulas.triangular(min_val=14, mode_val=21, max_val=35)
# Returns: IF(RAND()<(21-14)/(35-14),14+SQRT(RAND()*(35-14)*(21-14)),...)

# Triangular with named ranges
formula = DistributionFormulas.triangular_named(
    min_name="Tri_Season_Extension_Days_Min",
    mode_name="Tri_Season_Extension_Days_Mode",
    max_name="Tri_Season_Extension_Days_Max",
    rand_cell="B5"
)

# From a Variable object
formula = DistributionFormulas.from_variable(var, rand_cell="B5")
```

## Sheet Integration

### 4_Assumptions (Timing/Site/Costs)

Variables from `timing`, `site`, and `costs` categories are written to the Assumptions sheet:

```python
# In create_4_assumptions():
registry = get_registry()
timing_vars = registry.get_by_category('timing')

for var in timing_vars:
    ws.cell(row=row, column=1, value=var.id)
    ws.cell(row=row, column=2, value=var.params.get('value', 0))
    ws.cell(row=row, column=3, value=var.unit)
    ws.cell(row=row, column=4, value=var.params.get('notes', ''))
    add_named_range(wb, var.id, "4_Assumptions", f"$B${row}")
```

### 7_ServiceModels (Distribution Parameters)

Financial variables with triangular/beta distributions are written with their distribution parameters:

```python
# Triangular distributions
tri_vars = [v for v in registry.get_by_category('financial')
            if v.distribution == 'triangular']

for var in tri_vars:
    # Write min/mode/max values to columns B/C/D
    ws.cell(row=row, column=2, value=var.params['min'])
    ws.cell(row=row, column=3, value=var.params['mode'])
    ws.cell(row=row, column=4, value=var.params['max'])

    # Create named ranges for each parameter
    add_named_range(wb, f"Tri_{var.id}_Min", "7_ServiceModels", f"$B${row}")
    add_named_range(wb, f"Tri_{var.id}_Mode", "7_ServiceModels", f"$C${row}")
    add_named_range(wb, f"Tri_{var.id}_Max", "7_ServiceModels", f"$D${row}")
```

### 10_Calc_Stochastic (Formula Generation)

Stochastic formulas are generated using `DistributionFormulas`:

```python
for var in financial_vars:
    label = var.params.get('stoch_label', var.id)
    stoch_name = var.params.get('stoch_name', f"Stoch_{var.id}")

    ws.cell(row=row, column=1, value=label)
    ws.cell(row=row, column=2, value="=RAND()")

    if var.distribution == 'triangular':
        formula = DistributionFormulas.triangular_named(
            min_name=f"Tri_{var.id}_Min",
            mode_name=f"Tri_{var.id}_Mode",
            max_name=f"Tri_{var.id}_Max",
            rand_cell=f"B{row}"
        )

    ws.cell(row=row, column=3, value=f"={formula}")
    add_named_range(wb, stoch_name, "10_Calc_Stochastic", f"$C${row}")
```

## Stochastic Variable Configuration

Financial variables support additional params for stochastic sheet integration:

```yaml
- id: Season_Extension_Days
  distribution: triangular
  params:
    min: 14
    mode: 21
    max: 35
    stoch_name: Stoch_SeasonExt       # Named range for realized value
    stoch_label: Season_Extension      # Display label in stochastic sheet
```

| Param | Purpose | Default |
|-------|---------|---------|
| `stoch_name` | Named range for the realized stochastic value | `Stoch_{id}` |
| `stoch_label` | Display label in Variable column | `{id}` |

## INPUT_REGISTRY Generation

The `build_input_registry()` function dynamically generates mappings from input variables to the sheets that reference them:

```python
def build_input_registry(registry: VariableRegistry) -> dict:
    input_registry = {}

    # Financial triangular vars → Tri_{id}_* → 10_Calc_Stochastic
    for var in registry.get_by_category('financial'):
        if var.distribution == 'triangular':
            for suffix in ['Min', 'Mode', 'Max']:
                key = f"Tri_{var.id}_{suffix}"
                input_registry[key] = ['10_Calc_Stochastic']
        elif var.distribution == 'beta':
            for suffix in ['Min', 'Max']:
                key = f"Beta_{var.id}_{suffix}"
                input_registry[key] = ['10_Calc_Stochastic']

    # Kinetics baseline → 8_Calc_Timeline
    for var in registry.get_by_category('kinetics_baseline'):
        input_registry[var.id] = ['8_Calc_Timeline']

    return input_registry
```

This is merged with the manual `INPUT_REGISTRY` in `verify_traceability()` for validation.

## Validation

### Config Validation

```python
from variable_engine import ConfigValidator

validator = ConfigValidator()
errors = validator.validate_variable_file(Path("config/variables/timing.yaml"))
if errors:
    print("Validation errors:", errors)
```

### Traceability Verification

After workbook generation, `verify_traceability()` scans formula sheets to confirm that:
1. All registered inputs appear in expected sheets
2. Formula references match registry expectations

```python
verify_traceability(wb, fail_on_mismatch=False)
# Output: "Traceability verification: PASSED"
```

## Adding New Variables

### 1. Add to YAML Config

```yaml
# config/variables/timing.yaml
variables:
  - id: New_Timing_Var
    name: New Timing Variable
    unit: days
    distribution: fixed
    params:
      value: 10
      notes: Description
    sheet: 4_Assumptions
    is_input: true
```

### 2. Verify Category

Ensure the category exists in `validators.py:VALID_CATEGORIES`.

### 3. Test Loading

```bash
python -c "
from variable_engine import VariableRegistry
r = VariableRegistry()
r.load_config()
print(r.get('New_Timing_Var'))
"
```

### 4. Run Tests

```bash
pytest utils/financial_modeling/tests -v
```

## File Reference

| File | Purpose |
|------|---------|
| `variable_engine/__init__.py` | Public API: `VariableRegistry`, `DistributionFormulas`, `ConfigValidator` |
| `variable_engine/registry.py` | `Variable` dataclass and `VariableRegistry` class |
| `variable_engine/distributions.py` | Excel formula generators for all distribution types |
| `variable_engine/validators.py` | YAML schema validation and `VALID_CATEGORIES` |
| `config/variables/*.yaml` | Variable definitions by category |

## Deferred Features

The following are not yet registry-driven (kept as hardcoded for complexity reasons):

- **Learning Curve** (4_Assumptions): Complex time series structure
- **Test Options** (4_Assumptions): Specialized multi-column layout
- **Latency Gating** (4_Assumptions): Formula-driven, not data
- **Seasonality Table** (4_Assumptions): Monthly multiplier array
- **Value Sensitivity Table** (7_ServiceModels): Frame-based sensitivity analysis
