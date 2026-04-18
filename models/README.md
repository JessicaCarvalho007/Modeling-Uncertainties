# Models

This folder is for groundwater model files, model workspaces, and model-specific notes.

This repository is set up to use MODFLOW and PEST++ executables from the active Conda environment instead of storing executable files directly inside the repository.

## Activate the environment first

Before running any model scripts or notebooks, activate the project environment:

</> Bash

```bash
conda activate gw_uncertainty
```

## Finding the executable file paths

The shutil.which() function can be used to check where an executable is located

Executables installed:

**MODFLOW**
- mf6
- mf2005
- mfnwt
- mt3dms
- mp7
- gridgen
- zbud6

**PEST**
- pestpp-ies
- pestpp-glm
- pestpp-mou
- pestpp-opt
- pestpp-sen
- pestpp-swp
- pestpp-da
- pestpp-sqp

</> Python

```text
import shutil

for exe in ["mf6", "mf2005", "pestpp-ies", "pestpp-glm"]:
    exe_path = shutil.which(exe)
    print(f"{exe}: {exe_path}")
```

## Running MODFLOW

**Example: MODFLOW 6**

```text
import subprocess

subprocess.run(
    ["pestpp-ies", "my_model.pst"],
    cwd="models/my_pest_model",
    check=True
)
```
