# Deployment Commands - GitHub & PyPI

Complete guide with terminal commands to push your code to GitHub and publish to PyPI.

---

## Part 1: Push to GitHub

### Step 1: Initialize Git (if not already done)

```bash
cd /Users/opensource/Desktop/snakeskin-xplnhub-new

# Initialize git repository
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: Snakeskin framework with complete documentation"
```

### Step 2: Connect to GitHub Repository

```bash
# Add remote repository
git remote add origin https://github.com/XplnHUB/xplnhub-snakeskin.git

# Verify remote
git remote -v
```

### Step 3: Push to GitHub

```bash
# Push to main branch
git push -u origin main

# If the above fails (branch might be called 'master'), try:
git branch -M main
git push -u origin main
```

### Step 4: Push Future Updates

```bash
# After making changes
git add .
git commit -m "Your commit message here"
git push
```

---

## Part 2: Publish to PyPI

### Prerequisites

Install required tools:

```bash
pip install build twine
```

### Step 1: Clean Previous Builds

```bash
cd /Users/opensource/Desktop/snakeskin-xplnhub-new

# Remove old build artifacts
rm -rf build/ dist/ *.egg-info/
```

### Step 2: Build the Package

```bash
# Build distribution packages
python -m build
```

This creates:
- `dist/snakeskin_xplnhub-1.0.0-py3-none-any.whl` (wheel)
- `dist/snakeskin-xplnhub-1.0.0.tar.gz` (source)

### Step 3: Test on TestPyPI (Recommended)

```bash
# Upload to TestPyPI first
python -m twine upload --repository testpypi dist/*
```

You'll be prompted for:
- Username: `__token__`
- Password: Your TestPyPI API token (starts with `pypi-`)

Test installation:

```bash
# Test install from TestPyPI
pip install --index-url https://test.pypi.org/simple/ snakeskin-xplnhub
```

### Step 4: Publish to PyPI (Production)

```bash
# Upload to PyPI
python -m twine upload dist/*
```

You'll be prompted for:
- Username: `__token__`
- Password: Your PyPI API token (starts with `pypi-`)

### Step 5: Verify Installation

```bash
# Install from PyPI
pip install snakeskin-xplnhub

# Verify
snakeskin --version
```

---

## Complete Workflow (All Commands)

### First Time Setup

```bash
# Navigate to project
cd /Users/opensource/Desktop/snakeskin-xplnhub-new

# Git setup
git init
git add .
git commit -m "Initial commit: Snakeskin framework"
git remote add origin https://github.com/XplnHUB/xplnhub-snakeskin.git
git branch -M main
git push -u origin main

# Install build tools
pip install build twine

# Build package
python -m build

# Upload to TestPyPI (test first)
python -m twine upload --repository testpypi dist/*

# Test installation
pip install --index-url https://test.pypi.org/simple/ snakeskin-xplnhub

# If test successful, upload to PyPI
python -m twine upload dist/*
```

### Updating After Changes

```bash
# 1. Update version in setup.py (e.g., 1.0.0 -> 1.0.1)

# 2. Commit and push to GitHub
git add .
git commit -m "Version 1.0.1: Description of changes"
git push

# 3. Clean and rebuild
rm -rf build/ dist/ *.egg-info/
python -m build

# 4. Upload to PyPI
python -m twine upload dist/*
```

---

## Setting Up PyPI API Tokens

### For TestPyPI:

1. Go to https://test.pypi.org/manage/account/token/
2. Create a new API token
3. Copy the token (starts with `pypi-`)
4. Use it when prompted for password

### For PyPI:

1. Go to https://pypi.org/manage/account/token/
2. Create a new API token
3. Copy the token (starts with `pypi-`)
4. Use it when prompted for password

### Save Credentials (Optional)

Create `~/.pypirc`:

```bash
cat > ~/.pypirc << 'EOF'
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
username = __token__
password = pypi-YOUR_PYPI_TOKEN_HERE

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = pypi-YOUR_TESTPYPI_TOKEN_HERE
EOF

# Secure the file
chmod 600 ~/.pypirc
```

---

## Troubleshooting

### Git Issues

**Problem**: `fatal: remote origin already exists`

```bash
# Remove and re-add remote
git remote remove origin
git remote add origin https://github.com/XplnHUB/xplnhub-snakeskin.git
```

**Problem**: `! [rejected] main -> main (fetch first)`

```bash
# Pull first, then push
git pull origin main --rebase
git push
```

### PyPI Issues

**Problem**: `File already exists`

```bash
# You need to increment version in setup.py
# Change version="1.0.0" to version="1.0.1"
# Then rebuild and upload
```

**Problem**: `Invalid or non-existent authentication`

```bash
# Make sure you're using __token__ as username
# And your API token as password
# Token should start with pypi-
```

**Problem**: `Package name already taken`

```bash
# The package name 'snakeskin-xplnhub' should be available
# If not, you may need to choose a different name in setup.py
```

---

## Quick Reference

### GitHub Commands

```bash
# Status
git status

# Add files
git add .
git add filename.py

# Commit
git commit -m "message"

# Push
git push

# Pull
git pull

# View history
git log --oneline
```

### PyPI Commands

```bash
# Build
python -m build

# Upload to TestPyPI
python -m twine upload --repository testpypi dist/*

# Upload to PyPI
python -m twine upload dist/*

# Check package
twine check dist/*
```

---

## Verification Checklist

Before publishing:

- [ ] All tests pass
- [ ] Version number updated in `setup.py`
- [ ] `README.md` is up to date
- [ ] All documentation is correct
- [ ] GitHub repository URL is correct
- [ ] Package builds without errors: `python -m build`
- [ ] Package passes checks: `twine check dist/*`
- [ ] Tested on TestPyPI first
- [ ] Git changes committed and pushed

---

## Post-Deployment

After successful deployment:

### Verify GitHub

```bash
# Visit your repository
open https://github.com/XplnHUB/xplnhub-snakeskin
```

### Verify PyPI

```bash
# Visit your package page
open https://pypi.org/project/snakeskin-xplnhub/

# Test installation in a fresh environment
python -m venv test_env
source test_env/bin/activate
pip install snakeskin-xplnhub
snakeskin --version
deactivate
rm -rf test_env
```

### Create GitHub Release (Optional)

```bash
# Tag the release
git tag -a v1.0.0 -m "Release version 1.0.0"
git push origin v1.0.0
```

Then create a release on GitHub:
1. Go to https://github.com/XplnHUB/xplnhub-snakeskin/releases
2. Click "Create a new release"
3. Select the tag `v1.0.0`
4. Add release notes
5. Publish release

---

## Need Help?

- **Git Documentation**: https://git-scm.com/doc
- **PyPI Publishing Guide**: https://packaging.python.org/tutorials/packaging-projects/
- **Twine Documentation**: https://twine.readthedocs.io/

---

**Ready to deploy?** Start with the GitHub push, then test on TestPyPI before publishing to PyPI! 🚀
