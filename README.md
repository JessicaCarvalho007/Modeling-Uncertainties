# Modeling Uncertainties

Groundwater model uncertainty analysis repository using Python, Jupyter notebooks, FloPy, PyEMU, PyCAP-DSS, MODFLOW, and PEST++.

This repository is designed to support reproducible groundwater modeling workflows where model predictions are evaluated under uncertainty. The project is being developed for hydrogeology-focused analysis, including MODFLOW model runs, PyCAP-DSS analytical workflows, and PEST++/PyEMU uncertainty tools.

## Project Goals

This repository is intended to support:

- groundwater model setup, execution, and post-processing;
- MODFLOW 6 and MODFLOW-2005 workflows through FloPy;
- uncertainty analysis using PyEMU and PEST++;
- analytical capture/depletion-style calculations using PyCAP-DSS;
- reproducible Jupyter notebook workflows;
- reusable helper functions imported from a local Python package;
- clear organization of model inputs, outputs, figures, and results.

## Repository Structure

```text
Modeling-Uncertainties/
├── README.md
├── environment.yml
├── pyproject.toml
├── .gitignore
├── .vscode/
│   └── settings.json
├── setup/
│   ├── verify_setup.py
│   └── install_executables.sh
├── src/
│   └── gw_uncertainty/
│       ├── __init__.py
│       ├── paths.py
│       ├── modflow/
│       │   └── __init__.py
│       ├── pest/
│       │   └── __init__.py
│       └── pycap_tools/
│           └── __init__.py
├── notebooks/
├── data/
│   ├── raw/
│   └── processed/
├── models/
├── results/
├── figures/
├── docs/
└── scripts/
```

## Folder Descriptions

| Folder | Purpose |
|---|---|
| `notebooks/` | Main Jupyter notebook workflows for exploration, modeling, and analysis |
| `src/gw_uncertainty/` | Reusable Python helper code imported into notebooks |
| `setup/` | Environment checks and executable installation helpers |
| `models/` | MODFLOW, PEST++, and other model workspaces or model-specific notes |
| `data/raw/` | Original input data; large files should usually not be committed |
| `data/processed/` | Cleaned or processed data products |
| `results/` | Model outputs, uncertainty results, calibration results, and analysis products |
| `figures/` | Exported figures for reports, presentations, or papers |
| `docs/` | Project notes, methods, workflow documentation, and planning materials |
| `scripts/` | Optional command-line scripts, if needed later |

## Environment Approach

This repository uses a Conda environment with the `conda-forge` channel.

Conda is recommended because groundwater, geospatial, and uncertainty-analysis tools often rely on compiled dependencies. Packages such as GeoPandas, Rasterio, Fiona, GDAL, PyProj, FloPy, and PyEMU are usually easier to install consistently through Conda than through plain `pip`.

The main environment file is:

```text
environment.yml
```

## Create the Conda Environment

From the root of the repository, run:

```bash
conda env create -f environment.yml
```

Then activate the environment:

```bash
conda activate gw_uncertainty
```

If `conda activate` does not work in a GitHub Codespace, run:

```bash
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate gw_uncertainty
```

## Register the Jupyter Kernel

After activating the environment, register it as a Jupyter kernel:

```bash
python -m ipykernel install --user --name gw_uncertainty --display-name "Python (gw_uncertainty)"
```

When opening notebooks, select:

```text
Python (gw_uncertainty)
```

## Install This Repository as an Editable Package

This repository includes local helper code in:

```text
src/gw_uncertainty/
```

Install the repository in editable mode so notebooks can import from it:

```bash
python -m pip install -e .
```

Example notebook import:

```python
from gw_uncertainty.paths import PROJECT_ROOT, MODELS_DIR

print(PROJECT_ROOT)
print(MODELS_DIR)
```

The editable install means that future changes made inside `src/gw_uncertainty/` can be used by notebooks without reinstalling the full package.

## Install MODFLOW and PEST++ Executables

FloPy, PyEMU, and PyCAP-DSS are Python packages. MODFLOW and PEST++ are external executables that also need to be available.

With the `gw_uncertainty` environment active, run:

```bash
bash setup/install_executables.sh
```

This installs MODFLOW-related executables using `get-modflow` and PEST++ executables using `get-pestpp`.

Important distinction:

```text
FloPy = Python package used to build, run, and post-process MODFLOW models
MODFLOW = external groundwater model executable, such as mf6 or mf2005

PyEMU = Python package used for PEST/PEST++ workflows
PEST++ = external calibration and uncertainty executable suite
```

## Verify the Setup

After creating the environment, installing the editable package, and installing executables, run:

```bash
python setup/verify_setup.py
```

A successful setup should show that the main Python packages import correctly and that executables such as `mf6`, `pestpp-ies`, and `pestpp-glm` are available.

## Full First-Time Setup

For a new clone of this repository, the basic setup sequence is:

```bash
conda env create -f environment.yml
conda activate gw_uncertainty
python -m ipykernel install --user --name gw_uncertainty --display-name "Python (gw_uncertainty)"
python -m pip install -e .
bash setup/install_executables.sh
python setup/verify_setup.py
```

## Daily Workflow

After the repository has already been set up, the normal workflow is:

```bash
conda activate gw_uncertainty
jupyter lab
```

Or, to check the environment:

```bash
conda activate gw_uncertainty
python setup/verify_setup.py
```

## Using Local Helper Code in Notebooks

Reusable project code should go in:

```text
src/gw_uncertainty/
```

For example, future helper files may include:

```text
src/gw_uncertainty/modflow/runners.py
src/gw_uncertainty/pest/runners.py
src/gw_uncertainty/pycap_tools/depletion.py
```

Then notebooks can import from them using:

```python
from gw_uncertainty.modflow.runners import run_mf6_model
from gw_uncertainty.pest.runners import run_pestpp_ies
from gw_uncertainty.pycap_tools.depletion import calculate_depletion
```

## Using MODFLOW Executables

MODFLOW executables are installed into the active Conda environment, not stored directly in this repository.

For MODFLOW 6 with FloPy:

```python
import flopy

sim = flopy.mf6.MFSimulation(
    sim_name="my_model",
    exe_name="mf6",
    sim_ws="models/my_model"
)

success, buff = sim.run_simulation()

if not success:
    raise RuntimeError("MODFLOW 6 did not terminate normally.")
```

To check where an executable is located:

```python
import shutil

mf6_path = shutil.which("mf6")
print(mf6_path)
```

The same pattern works for other executables:

```python
import shutil

for exe in ["mf6", "mf2005", "pestpp-ies", "pestpp-glm"]:
    print(exe, shutil.which(exe))
```

Avoid hard-coding full executable paths because they may be different on another computer, operating system, or Codespace.

## Using PEST++

PEST++ executables are also installed into the active Conda environment.

Common PEST++ executables include:

```text
pestpp-glm
pestpp-ies
pestpp-mou
pestpp-opt
pestpp-sen
```

PEST++ usually requires a PEST control file with a `.pst` extension.

Example command-line usage:

```bash
pestpp-ies my_model.pst
```

or:

```bash
pestpp-glm my_model.pst
```

Example Python usage:

```python
import subprocess

subprocess.run(
    ["pestpp-ies", "my_model.pst"],
    cwd="models/my_pest_model",
    check=True
)
```

## Updating the Environment

When adding new Conda packages:

```bash
conda activate gw_uncertainty
conda install -c conda-forge package-name
conda env export --from-history > environment.yml
```

After exporting, check `environment.yml` before committing.

If a package must be installed with `pip`, add it under a `pip:` section in `environment.yml`.

## Notes on Large Files

Large model outputs, generated results, and temporary files should usually not be committed to GitHub. The `.gitignore` file is set up to avoid tracking common generated files from Python, Jupyter, MODFLOW, and PEST++ workflows.

Small example input files may be committed when they are needed to make the repository reproducible.

## Git Workflow

A common workflow after making changes is:

```bash
git status
git add .
git commit -m "Describe the change"
git push origin main
```

Before committing, check that large generated outputs are not being added accidentally.

## License

This repository uses the MIT License.
