"""
Integration modules for Snakeskin framework.
Provides helpers for Tailwind CSS and Bootstrap integration.
"""

import os
import shutil
from pathlib import Path

class TailwindIntegration:
    """Helper class for Tailwind CSS integration."""
    
    @staticmethod
    def setup(project_path):
        """Set up Tailwind CSS in a project."""
        config_path = Path(project_path) / "tailwind.config.js"
        input_path = Path(project_path) / "input.css"
        
        # Create tailwind.config.js if it doesn't exist
        if not config_path.exists():
            with open(config_path, "w") as f:
                f.write('module.exports = { content: ["./src/components/**/*.py", "./main.py"], theme: { extend: {}, }, plugins: [], };')
        
        # Create input.css if it doesn't exist
        if not input_path.exists():
            with open(input_path, "w") as f:
                f.write('@tailwind base;\n@tailwind components;\n@tailwind utilities;')
    
    @staticmethod
    def build(output_path="./dist/tailwind.css", minify=True):
        """Build Tailwind CSS."""
        minify_flag = "--minify" if minify else ""
        os.system(f"npx tailwindcss -i ./input.css -o {output_path} {minify_flag}")


class BootstrapIntegration:
    """Helper class for Bootstrap integration."""
    
    @staticmethod
    def setup(project_path):
        """Set up Bootstrap in a project."""
        bootstrap_dir = Path(project_path) / "dist" / "bootstrap"
        os.makedirs(bootstrap_dir, exist_ok=True)
        
        # Create index.html with Bootstrap CDN links if it doesn't exist
        index_path = Path(project_path) / "dist" / "index.html"
        if not index_path.exists():
            with open(index_path, "w") as f:
                f.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Snakeskin App with Bootstrap</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div id="app"></div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
""")
    
    @staticmethod
    def get_cdn_links():
        """Get Bootstrap CDN links for CSS and JS."""
        css = '<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">'
        js = '<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>'
        return {
            'css': css,
            'js': js
        }
    
    @staticmethod
    def include_in_template(template, position="head"):
        """Include Bootstrap in an HTML template."""
        links = BootstrapIntegration.get_cdn_links()
        
        if position == "head":
            # Add CSS to head
            if "</head>" in template:
                return template.replace("</head>", f"{links['css']}\n</head>")
            else:
                return f"{links['css']}\n{template}"
        elif position == "body":
            # Add JS before end of body
            if "</body>" in template:
                return template.replace("</body>", f"{links['js']}\n</body>")
            else:
                return f"{template}\n{links['js']}"
        elif position == "both":
            # Add both CSS and JS
            template = BootstrapIntegration.include_in_template(template, "head")
            template = BootstrapIntegration.include_in_template(template, "body")
            return template
        
        return template
