# Quick Deploy Reference

## 🚀 Option 1: Use the Deploy Script (Easiest)

```bash
./deploy.sh
```

Then follow the interactive prompts!

---

## 📝 Option 2: Manual Commands

### Push to GitHub

```bash
# First time
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/XplnHUB/xplnhub-snakeskin.git
git branch -M main
git push -u origin main

# Updates
git add .
git commit -m "Your message"
git push
```

### Publish to PyPI

```bash
# Install tools (first time only)
pip install build twine

# Clean and build
rm -rf build/ dist/ *.egg-info/
python -m build

# Test on TestPyPI
python -m twine upload --repository testpypi dist/*

# Publish to PyPI
python -m twine upload dist/*
```

---

## 🔑 PyPI Credentials

When prompted:
- **Username**: `__token__`
- **Password**: Your API token (get from pypi.org)

---

## 📚 Full Documentation

See [DEPLOYMENT_COMMANDS.md](DEPLOYMENT_COMMANDS.md) for complete details.
