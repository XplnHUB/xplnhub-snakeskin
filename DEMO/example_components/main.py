from src.components.Navbar import Navbar
from src.components.Hero import Hero
from src.components.Features import Features
from src.components.ContactForm import ContactForm
from src.components.Footer import Footer

# Initialize components
navbar = Navbar()
hero = Hero()
features = Features()
contact = ContactForm()
footer = Footer()

# Mount components to activate lifecycle hooks
navbar.mount()
hero.mount()
features.mount()
contact.mount()
footer.mount()

# Create HTML content
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Snakeskin - Modern Python Web Framework</title>
    <link href="tailwind.css" rel="stylesheet">
    <style>
        html {{
            scroll-behavior: smooth;
        }}
    </style>
</head>
<body class="bg-gray-50">
    {navbar.render()}
    {hero.render()}
    {features.render()}
    {contact.render()}
    {footer.render()}
</body>
</html>
"""

# Write to file
with open("dist/index.html", "w") as f:
    f.write(html_content)

print("✅ Build complete! Open dist/index.html to view your landing page.")
