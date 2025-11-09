from setuptools import setup, find_packages

setup(
    name="snakeskin-xplnhub",
    version="1.0.1",
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
    description="A Python framework for modular site generation",
    author="Arpit Sarang",
    license="MIT",
)
