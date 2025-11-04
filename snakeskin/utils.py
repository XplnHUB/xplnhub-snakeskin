import os
import shutil
import subprocess

TEMPLATE_COMPONENT = '''from snakeskin.framework import Component
class App(Component):
    def render(self):
        return """
        <section class="flex flex-col items-center justify-center min-h-screen bg-gray-100">
            <h1 class="text-4xl font-bold text-blue-600">Welcome to Snakeskin!</h1>
            <p class="mt-4 text-lg text-gray-700">Your modern Python framework.</p>
        </section>
        """ 
'''

TEMPLATE_MAIN = '''from src.components.App import App
app = App()
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Snakeskin App</title>
    <link href="tailwind.css" rel="stylesheet"> 
</head>
<body>
    {app.render()}
</body>
</html>
"""

with open("dist/index.html", "w") as f:
    f.write(html_content)
print("Build complete! Open dist/index.html to view your app.")
'''

def create_project(name):
    """Scaffold a new Snakeskin project"""
    os.makedirs(f"{name}/src/components", exist_ok=True)
    os.makedirs(f"{name}/dist", exist_ok=True)

    with open(f"{name}/src/components/App.py", "w") as f:
        f.write(TEMPLATE_COMPONENT)

    with open(f"{name}/main.py", "w") as f:
        f.write(TEMPLATE_MAIN)
    
    with open(f"{name}/tailwind.config.js", "w") as f:
        f.write('module.exports = { content: ["./src/components/**/*.py", "./main.py"], theme: { extend: {}, }, plugins: [], };')
    
    # Create input.css file for Tailwind CSS
    with open(f"{name}/input.css", "w") as f:
        f.write('@tailwind base;\n@tailwind components;\n@tailwind utilities;')

    print(f"Project '{name}' scaffolded successfully")


def build_project():
    """Build project into dist folder with proper error handling"""
    
    print("Building Project....")
    
    try:
        # Ensure dist directory exists
        os.makedirs("dist", exist_ok=True)
        
        # Run main.py to generate HTML
        main_result = subprocess.run(
            ["python", "main.py"],
            capture_output=True,
            text=True,
            check=True
        )
        
        # Process Tailwind CSS
        if os.path.exists("input.css"):
            tailwind_result = subprocess.run(
                ["npx", "tailwindcss", "-i", "./input.css", "-o", "./dist/tailwind.css", "--minify"],
                capture_output=True,
                text=True,
                check=True
            )
        else:
            print("Warning: input.css not found. Skipping Tailwind processing.")
        
        # Optimize images if available
        if os.path.exists("src/assets"):
            print("Copying and optimizing assets...")
            os.makedirs("dist/assets", exist_ok=True)
            for file in os.listdir("src/assets"):
                shutil.copy2(f"src/assets/{file}", f"dist/assets/{file}")
        
        print("Build completed! Files ready in ./dist")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"Error during build: {e}")
        print(f"Command output: {e.output}")
        print(f"Command stderr: {e.stderr}")
        return False
    except Exception as e:
        print(f"Unexpected error during build: {e}")
        return False
    