from setuptools import setup, find_packages

# Read the contents of the README file
with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="snakeskin-xplnhub",
    version="1.0.2",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "rich",
        "typer",
        "watchdog",
        "websockets",
        "click",
        "markdown-it-py",
        "shellingham",
    ],
    python_requires=">=3.8",
    description="A modern, lightweight frontend framework for building component-based web applications",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Arpit Sarang",
    author_email="info@snakeskin-framework.dev",
    url="https://github.com/XplnHUB/xplnhub-snakeskin",
    project_urls={
        "Documentation": "https://github.com/XplnHUB/xplnhub-snakeskin/tree/main/docs",
        "Bug Reports": "https://github.com/XplnHUB/xplnhub-snakeskin/issues",
        "Source Code": "https://github.com/XplnHUB/xplnhub-snakeskin",
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: User Interfaces",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    keywords="web, frontend, framework, component, ui, tailwind, bootstrap, modular, site-generation",
    license="MIT",
)
