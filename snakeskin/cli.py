import typer 
from snakeskin.utils import create_project , build_project
from snakeskin.server import run_dev_server

app = typer.Typer(help="Snakeskin - A venomously fast frontend framework written in Python")

@app.command()
def create(name: str):
    """Create a new Snakeskin project"""
    create_project(name)    
    typer.echo(f"🐍 Project '{name}' has slithered into existence! Venomously fast development awaits.")

@app.command()
def build():
    """Build the Snakeskin project"""
    build_project()
    typer.echo("🐍 Your project has shed its skin! Optimized build ready to strike in ./dist")

@app.command()
def dev():
    """Run the development server"""
    run_dev_server()
    typer.echo("🐍 Development server coiled and ready to strike! Hot reload activated with venomous speed.")

@app.command()
def deploy(provider: str = typer.Argument(..., help="Deployment provider: 'vercel' or 'netlify'")):
    """Deploy the project to Vercel or Netlify (Coming soon)"""
    # This is a placeholder for future implementation
    if provider.lower() not in ['vercel', 'netlify']:
        typer.echo(f"🐍 Error: Unknown provider '{provider}'. Use 'vercel' or 'netlify'.")
        raise typer.Exit(1)
    
    typer.echo(f"🐍 Preparing to deploy to {provider}...")
    typer.echo("🐍 This feature is coming in a future version. For now, please follow the deployment guides:")
    typer.echo("   - Vercel: See docs/vercel_deployment.md")
    typer.echo("   - Netlify: See docs/netlify_deployment.md")

@app.callback()
def main(
    version:bool = typer.Option(
        False, "--version", "-v", help="Show the version of Snakeskin"
    )
): 
    if version:
        typer.echo("🐍 Snakeskin version 1.0.0 - Venomously fast web development")
        raise typer.Exit()

if __name__ == "__main__":
    app()