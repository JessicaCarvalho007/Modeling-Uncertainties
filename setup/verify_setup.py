"""Verify the main Python packages for the Modeling-Uncertainties repository.

Run from the repository root after activating the environment:

    conda activate gw_uncertainty
    python scripts/verify_setup.py
"""

from __future__ import annotations

import importlib
import shutil
import sys


PACKAGE_IMPORTS = {
    "numpy": "numpy",
    "pandas": "pandas",
    "scipy": "scipy",
    "matplotlib": "matplotlib",
    "flopy": "flopy",
    "pyemu": "pyemu",
    "pycap": "pycap",  # installed as pycap-dss, imported as pycap
    "geopandas": "geopandas",
    "shapely": "shapely",
    "pyproj": "pyproj",
    "rasterio": "rasterio",
    "yaml": "yaml",  # installed as pyyaml
    "requests": "requests",
    "openpyxl": "openpyxl",
}


def check_import(display_name: str, import_name: str) -> bool:
    """Try to import a package and print its version when available."""
    try:
        module = importlib.import_module(import_name)
    except Exception as err:
        print(f"[FAIL] {display_name:12s} could not be imported: {err}")
        return False

    version = getattr(module, "__version__", "version not reported")
    print(f"[ OK ] {display_name:12s} {version}")
    return True


def check_executable(executable_name: str) -> None:
    """Check whether an external executable is visible on PATH."""
    path = shutil.which(executable_name)
    if path:
        print(f"[ OK ] executable {executable_name!r} found at: {path}")
    else:
        print(f"[WARN] executable {executable_name!r} not found on PATH")


def main() -> int:
    print("\nPython executable:")
    print(sys.executable)

    print("\nPython version:")
    print(sys.version)

    print("\nChecking Python packages:")
    results = [
        check_import(display_name, import_name)
        for display_name, import_name in PACKAGE_IMPORTS.items()
    ]

    print("\nChecking optional external executables:")
    check_executable("mf6")
    check_executable("pestpp-ies")
    check_executable("pestpp-glm")

    failed = [ok for ok in results if not ok]
    if failed:
        print("\nSome Python package imports failed.")
        return 1

    print("\nEnvironment check complete.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
