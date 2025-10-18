import os
import shutil

TEMPLATE_COMPONENT = '''from mamba.framework import Component
class App(Component):
    def render(self):
        return """
        <section class="flex flex-col items-center justify-center min-h-screen bg-gray-100">
            <h1 class="text-4xl font-bold text-blue-600">Welcome to Mamba.py!</h1>
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
    <title>Mamba.py App</title>
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
    """Scaffold a new Mamba.py project"""
    os.makedirs(f"{name}/src/components",exits_ok=True)
    os.makedirs(f"{name}/dist",exits_ok=True)

    with open(f"{name}/src/components/App.py", "w") as f:
        f.write(TEMPLATE_COMPONENT)

    with open(f"{name}/main.py", "w") as f:
        f.write(TEMPLATE_MAIN)
    
    with open(f"{name}/tailwind.config.js", "w") as f:
        f.write('module.exports = { content: ["./src/components/**/*.py", "./main.py"], theme: { extend: {}, }, plugins: [], };')

    print(f"Project '{name}'scaffolded sucessfully")


def build_project():
    "Build project into dist folder"

    print("Building Project....")

    os.system("python main.py")
    os.system("npx tailwindcss -i ./input.css -o ./dist/tailwind.css --mainfy")

    print("Build completed! Files ready in ./dist")

    