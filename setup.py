from setuptools import setup, find_packages
import os

# Read the contents of the README file
with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="snakeskin-xplnhub",
    version="1.0.0",
    description="A modern, lightweight frontend framework for building component-based web applications",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Snakeskin Team",
    author_email="info@snakeskin-framework.dev",
    url="https://github.com/XplnHUB/xplnhub-snakeskin",
    project_urls={
        "Documentation": "https://github.com/XplnHUB/xplnhub-snakeskin/tree/main/docs",
        "Bug Reports": "https://github.com/XplnHUB/xplnhub-snakeskin/issues",
        "Source Code": "https://github.com/XplnHUB/xplnhub-snakeskin",
    },
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "typer>=0.4.0",
        "watchdog>=2.1.0",  # For file watching and hot reload
    ],
    extras_require={
        "dev": [
            "websockets>=10.0",  # For WebSocket-based hot reload
        ],
        "bootstrap": [
            # Bootstrap integration dependencies
        ],
    },
    entry_points={
        "console_scripts":[
            "snakeskin = snakeskin.cli:app"
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: User Interfaces",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    keywords="web, frontend, framework, component, ui, tailwind, bootstrap",
    python_requires=">=3.7",
    license="MIT",
)
