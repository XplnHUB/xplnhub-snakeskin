#!/bin/bash

# Snakeskin Deployment Script
# This script helps deploy to GitHub and PyPI

set -e  # Exit on error

echo "🐍 Snakeskin Deployment Script"
echo "================================"
echo ""

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print colored output
print_success() {
    echo -e "${GREEN}✓ $1${NC}"
}

print_error() {
    echo -e "${RED}✗ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠ $1${NC}"
}

print_info() {
    echo -e "${YELLOW}ℹ $1${NC}"
}

# Check if we're in the right directory
if [ ! -f "setup.py" ]; then
    print_error "setup.py not found. Please run this script from the project root."
    exit 1
fi

# Main menu
echo "What would you like to do?"
echo "1) Push to GitHub"
echo "2) Publish to PyPI (TestPyPI first, then PyPI)"
echo "3) Both (GitHub + PyPI)"
echo "4) Clean build artifacts"
echo "5) Exit"
echo ""
read -p "Enter your choice (1-5): " choice

case $choice in
    1)
        echo ""
        echo "📦 Pushing to GitHub..."
        echo "======================="
        
        # Check if git is initialized
        if [ ! -d ".git" ]; then
            print_info "Initializing git repository..."
            git init
        fi
        
        # Check if remote exists
        if ! git remote | grep -q "origin"; then
            print_info "Adding remote origin..."
            git remote add origin https://github.com/XplnHUB/xplnhub-snakeskin.git
        fi
        
        # Get commit message
        read -p "Enter commit message: " commit_msg
        
        # Add, commit, and push
        git add .
        git commit -m "$commit_msg"
        git branch -M main
        git push -u origin main
        
        print_success "Successfully pushed to GitHub!"
        ;;
        
    2)
        echo ""
        echo "📦 Publishing to PyPI..."
        echo "========================"
        
        # Check if build tools are installed
        if ! command -v twine &> /dev/null; then
            print_warning "Installing build tools..."
            pip install build twine
        fi
        
        # Clean old builds
        print_info "Cleaning old build artifacts..."
        rm -rf build/ dist/ *.egg-info/
        
        # Build package
        print_info "Building package..."
        python -m build
        
        # Check package
        print_info "Checking package..."
        twine check dist/*
        
        # Upload to TestPyPI
        echo ""
        print_warning "Uploading to TestPyPI first for testing..."
        echo "You'll need your TestPyPI API token."
        echo "Username: __token__"
        echo "Password: (your TestPyPI token)"
        echo ""
        
        python -m twine upload --repository testpypi dist/*
        
        print_success "Uploaded to TestPyPI!"
        echo ""
        print_info "Test installation with:"
        echo "pip install --index-url https://test.pypi.org/simple/ snakeskin-xplnhub"
        echo ""
        
        read -p "Did TestPyPI installation work? Upload to PyPI? (y/n): " upload_pypi
        
        if [ "$upload_pypi" = "y" ] || [ "$upload_pypi" = "Y" ]; then
            echo ""
            print_warning "Uploading to PyPI..."
            echo "You'll need your PyPI API token."
            echo "Username: __token__"
            echo "Password: (your PyPI token)"
            echo ""
            
            python -m twine upload dist/*
            
            print_success "Successfully published to PyPI!"
            echo ""
            print_info "Install with: pip install snakeskin-xplnhub"
        else
            print_warning "Skipped PyPI upload."
        fi
        ;;
        
    3)
        echo ""
        echo "📦 Deploying to GitHub and PyPI..."
        echo "==================================="
        
        # GitHub first
        print_info "Step 1: Pushing to GitHub..."
        
        if [ ! -d ".git" ]; then
            git init
        fi
        
        if ! git remote | grep -q "origin"; then
            git remote add origin https://github.com/XplnHUB/xplnhub-snakeskin.git
        fi
        
        read -p "Enter commit message: " commit_msg
        
        git add .
        git commit -m "$commit_msg"
        git branch -M main
        git push -u origin main
        
        print_success "Pushed to GitHub!"
        
        # PyPI
        echo ""
        print_info "Step 2: Publishing to PyPI..."
        
        if ! command -v twine &> /dev/null; then
            pip install build twine
        fi
        
        rm -rf build/ dist/ *.egg-info/
        python -m build
        twine check dist/*
        
        echo ""
        print_warning "Uploading to TestPyPI..."
        python -m twine upload --repository testpypi dist/*
        
        print_success "Uploaded to TestPyPI!"
        echo ""
        
        read -p "Upload to PyPI? (y/n): " upload_pypi
        
        if [ "$upload_pypi" = "y" ] || [ "$upload_pypi" = "Y" ]; then
            python -m twine upload dist/*
            print_success "Successfully deployed to GitHub and PyPI!"
        else
            print_warning "Deployed to GitHub only."
        fi
        ;;
        
    4)
        echo ""
        echo "🧹 Cleaning build artifacts..."
        rm -rf build/ dist/ *.egg-info/
        print_success "Build artifacts cleaned!"
        ;;
        
    5)
        echo "Goodbye! 👋"
        exit 0
        ;;
        
    *)
        print_error "Invalid choice. Please run the script again."
        exit 1
        ;;
esac

echo ""
echo "================================"
print_success "Done! 🎉"
