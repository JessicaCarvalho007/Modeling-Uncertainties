#!/usr/bin/env bash

# Install external groundwater modeling executables into the active Conda environment.
# This installs MODFLOW-related executables using FloPy's get-modflow utility
# and PEST++ executables using PyEMU's get-pestpp utility.

set -euo pipefail

ENV_NAME="gw_uncertainty"

echo "Checking active Conda environment..."

if [[ "${CONDA_DEFAULT_ENV:-}" != "$ENV_NAME" ]]; then
    echo "ERROR: Please activate the $ENV_NAME environment first:"
    echo ""
    echo "    conda activate $ENV_NAME"
    echo ""
    exit 1
fi

echo "Active environment: $CONDA_DEFAULT_ENV"
echo ""

echo "Installing MODFLOW executables..."
get-modflow :python

echo ""
echo "Installing PEST++ executables..."
get-pestpp :python

echo ""
echo "Verifying setup..."
python setup/verify_setup.py

echo ""
echo "Executable installation complete."
