# PyPI Deployment Guide

This guide explains how to deploy the Snakeskin package to PyPI.

GitHub Repository: [https://github.com/XplnHUB/xplnhub-snakeskin](https://github.com/XplnHUB/xplnhub-snakeskin)

## Prerequisites

1. Create an account on [PyPI](https://pypi.org/) if you don't have one
2. Install required tools:
   ```bash
   pip install build twine
   ```

## Deployment Steps

1. Update version number in `setup.py`
2. Create your `.pypirc` file from the template:
   ```bash
   cp .pypirc.template ~/.pypirc
   ```
3. Edit `~/.pypirc` and add your PyPI token
4. Build the package:
   ```bash
   python -m build
   ```
5. Upload to TestPyPI first (recommended):
   ```bash
   python -m twine upload --repository testpypi dist/*
   ```
6. Test the installation:
   ```bash
   pip install --index-url https://test.pypi.org/simple/ snakeskin
   ```
7. Upload to PyPI:
   ```bash
   python -m twine upload dist/*
   ```

## Cleaning Up

After successful deployment, you can clean up build files:
```bash
rm -rf build/ dist/ *.egg-info/
```
