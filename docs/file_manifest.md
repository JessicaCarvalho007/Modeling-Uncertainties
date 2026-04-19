# Little Plover River Model File Manifest

This file tracks the Little Plover River model files copied into this repository.

## Source repository

Original source:

https://github.com/mnfienen/LPR_redux

The files were copied into this repository so this project can use the Little Plover River MODFLOW 6 model and PyCAP analytical model in a cleaner uncertainty-analysis workflow.

## Copied folders

| New location | Source location | Purpose |
|---|---|---|
| `models/lpr_mf6/steady_state/` | `LPR_MODFLOW/steady_state_mf6/` | MODFLOW 6 steady-state Little Plover River model |
| `data/raw/lpr_pycap/pycap_base/` | `LPR_pycap_opt/pycap_runs/pycap_base/` | Baseline PyCAP configuration and output files |
| `data/raw/lpr_pycap/inputs/` | `LPR_pycap_opt/Inputs/` | Excel and CSV input files used to build or analyze the PyCAP model |
| `scripts/lpr_legacy/` | `LPR_pycap_opt/scripts/` | Original PyCAP/Pest++ helper scripts copied for reference and later refactoring |

## Notes

The files in `scripts/lpr_legacy/` should be treated as reference scripts, not final project code. They may contain hard-coded relative paths from the original `LPR_redux` repository structure.

Future project-specific code should be rebuilt in `src/gw_uncertainty/` and called from clean notebooks.
