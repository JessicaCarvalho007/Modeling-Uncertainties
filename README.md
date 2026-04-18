# Modeling Uncertainties

Groundwater model uncertainty analysis repository using Python, Jupyter notebooks, FloPy, PyEMU, PyCAP-DSS, MODFLOW, and PEST++.

This repository is designed to be reproducible, reusable, and easy to fork. The main goal is to support groundwater modeling workflows where model predictions are tested under uncertainty, including parameter uncertainty, model calibration uncertainty, and prediction uncertainty.

## Project goals

This repository will support workflows such as:

- building and running groundwater models with MODFLOW and FloPy,
- analyzing groundwater model uncertainty,
- using PyEMU and PEST++ for calibration and uncertainty analysis,
- using PyCAP-DSS for analytical capture/depletion-style calculations,
- running reproducible Jupyter notebook workflows,
- organizing model inputs, outputs, figures, and results in a clear project structure.

## Environment approach

This project uses a Conda environment with the conda-forge channel.

Conda is recommended for this repository because groundwater and geospatial modeling packages often rely on compiled dependencies. Packages such as GeoPandas, Rasterio, Fiona, GDAL, PyProj, FloPy, and PyEMU are usually easier to install and maintain through Conda than through plain pip.

## Repository structure

```text
Modeling-Uncertainties/
├── README.md
├── environment.yml
├── .gitignore
├── setup/
│   ├── verify_setup.py
│   └── install_executables.sh
├── notebooks/
├── data/
│   ├── raw/
│   └── processed/
├── models/
├── results/
├── figures/
└── docs/
```

## Folder notes

- `notebooks/` — Jupyter notebooks for exploration, analysis, and figures.
- `scripts/` — reusable Python scripts.
- `data/raw/` — original input data. Large files should usually not be committed.
- `data/processed/` — cleaned or processed data products.
- `models/` — model input files or small example model files.
- `results/` — model outputs, uncertainty results, calibration outputs.
- `figures/` — exported figures for reports, presentations, or papers.
- `docs/` — notes, methods, diagrams, and project documentation.
- `setup/` — Environment checks and installation helper scripts.

## License

 MIT License 