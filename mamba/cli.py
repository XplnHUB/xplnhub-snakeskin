import typer 
from mamba.utils import create_project , build_project
from mamba.server import run_dev_server

app = typer.Typer(help="Mamba.py - A modern framerwork written in Python")

@app.command()
def create(name: str):
    """Create a new Mamba.py project"""
    create_project(name)    
    typer.echo(f"Project '{name}' created successfully.")

@app.command()
def build():
    """Build the Mamba.py project"""
    build_project()
    typer.echo("Project built successfully.")

@app.command()
def dev():
    """Run the development server"""
    run_dev_server()
    typer.echo("Development server is running...")

@app.callback()
def main(
    version:bool = typer.Option(
        False, "--version", "-v", help="Show the version of Mamba.py"
    )
): 
    if version:
        typer.echo("Mamba.py version 1.0.0")
        raise typer.Exit()

if __name__ == "__main__":
    app()