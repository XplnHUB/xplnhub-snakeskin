# Package Structure

This document explains the structure of the Snakeskin package and which files are essential for PyPI.

GitHub Repository: [https://github.com/XplnHUB/xplnhub-snakeskin](https://github.com/XplnHUB/xplnhub-snakeskin)

## Essential Files for PyPI

- **`setup.py`**: Main package configuration
- **`setup.cfg`**: Additional package configuration
- **`pyproject.toml`**: Modern Python packaging configuration
- **`MANIFEST.in`**: Controls what files are included in the package
- **`LICENSE`**: License information (required by PyPI)
- **`README.md`**: Package description and documentation
- **`snakeskin/`**: The actual package code

## Optional Files (Not Uploaded to PyPI)

- **`.git/`**: Git repository data
- **`.gitignore`**: Git ignore rules
- **`docs/`**: Documentation files (excluded via MANIFEST.in)
- **`.pypirc.template`**: Template for PyPI upload configuration
- **`PYPI_DEPLOYMENT.md`**: Deployment instructions
- **`PACKAGE_STRUCTURE.md`**: This file
- **`Report.md`**: Development report (deleted)

## Files Created/Modified

1. Created `.gitignore` to exclude unnecessary files from version control
2. Created `MANIFEST.in` to control what files are included in the package
3. Created `LICENSE` file (required by PyPI)
4. Updated `setup.py` with additional metadata for PyPI
5. Created `setup.cfg` for additional package configuration
6. Created `.pypirc.template` for PyPI upload configuration
7. Created `pyproject.toml` for modern Python packaging
8. Created `PYPI_DEPLOYMENT.md` with deployment instructions
9. Removed `Report.md` as it's not needed for PyPI
10. Created `docs/index.md` to organize documentation

## Files to Delete Before Upload

The following files are not needed for PyPI and can be deleted before upload:

- `.pypirc.template` (contains sensitive information template)
- `PYPI_DEPLOYMENT.md` (internal documentation)
- `PACKAGE_STRUCTURE.md` (this file)

## How to Clean Up Before Building

```bash
# Remove unnecessary files
rm -rf .git
rm -f .pypirc.template PYPI_DEPLOYMENT.md PACKAGE_STRUCTURE.md

# Remove any build artifacts
rm -rf build/ dist/ *.egg-info/
```
