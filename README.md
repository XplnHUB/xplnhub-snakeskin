# snakeskin-xplnhub

<div align="center">
  <img src="https://github.com/user-attachments/assets/2106926b-992a-4921-a982-19046c1122bf" width="180" />
</div>


Snakeskin is a **modern, lightweight frontend framework/library** designed to make building **component-based web applications** fast, flexible, and enjoyable. It integrates seamlessly with **Tailwind CSS** and **Bootstrap**, and provides a **CLI tool** to scaffold, run, and build projects effortlessly. Snakeskin is designed to be **AI-ready and backend-friendly** for future integrations

<div align="center">
  
[![PyPI Downloads](https://static.pepy.tech/personalized-badge/snakeskin-xplnhub?period=total&units=INTERNATIONAL_SYSTEM&left_color=BLACK&right_color=GREEN&left_text=Total+Downloads)](https://pepy.tech/projects/snakeskin-xplnhub)
[![PyPI Downloads](https://static.pepy.tech/personalized-badge/snakeskin-xplnhub?period=monthly&units=INTERNATIONAL_SYSTEM&left_color=BLACK&right_color=RED&left_text=Monthly+Downloads)](https://pepy.tech/projects/snakeskin-xplnhub)
[![PyPI Downloads](https://static.pepy.tech/personalized-badge/snakeskin-xplnhub?period=weekly&units=INTERNATIONAL_SYSTEM&left_color=BLACK&right_color=BLUE&left_text=Weekly+Downloads)](https://pepy.tech/projects/snakeskin-xplnhub)
  
</div>

---
## [Help us to imporve](https://forms.gle/N9iAzTtqpyRfP8MK9)
---

## Features

- **Component-Based Architecture**: Build reusable UI components easily.  
- **State Management**: Reactive state system with lifecycle hooks.  
- **Tailwind CSS & Bootstrap Integration**: Style your apps with your favorite frameworks.  
- **CLI Tooling**:
  - `snakeskin create <project-name>` → Scaffold a new project  
  - `snakeskin dev` → Start a local development server with hot reload  
  - `snakeskin build` → Generate production-ready build  
- **Fast Development & Deployment**: Optimized build system and CLI for Vercel/Netlify deployments.  
- **Future-Ready**: Planned support for backend integrations, AI models, and databases.  

---

## Installation

```bash
pip install snakeskin-xplnhub
```

For development features including hot reload:

```bash
pip install snakeskin-xplnhub[dev]
```

For Bootstrap integration:

```bash
pip install snakeskin-xplnhub[bootstrap]
```

> **Note**: Snakeskin is written in Python and provides a lightweight frontend runtime. Future versions may include a full JS/TS runtime for advanced features.

---

## Quick Start

### 1. Create a New Project

```bash
snakeskin create my-landing-page
cd my-landing-page
```

### 2. Add Components

```python
# src/components/Hero.py
from snakeskin.framework import Component

class Hero(Component):
    def __init__(self, **props):
        super().__init__(**props)
        self.state = {
            "clicked": False
        }
    
    def handle_click(self):
        self.set_state({"clicked": not self.state.get("clicked", False)})
    
    def render(self):
        button_class = "bg-blue-500 text-white px-6 py-3 rounded hover:bg-blue-600"
        if self.state.get("clicked", False):
            button_class = "bg-green-500 text-white px-6 py-3 rounded hover:bg-green-600"
            
        return f"""
        <section class="text-center py-20 bg-gray-100">
            <h1 class="text-5xl font-bold mb-4">Welcome to Snakeskin</h1>
            <p class="text-gray-600 mb-6">Build modern web apps effortlessly.</p>
            <button class="{button_class}" onclick="handleClick_{id(self)}()">
                Get Started
            </button>
            <script>
                function handleClick_{id(self)}() {{
                    console.log("Button clicked");
                    // In a real app, you would use AJAX or WebSockets
                }}
            </script>
        </section>
        """
```

### 3. Compose Components

```python
# main.py
from src.components.Navbar import Navbar
from src.components.Hero import Hero
from snakeskin import BootstrapIntegration

# Initialize components
navbar = Navbar(title="Snakeskin")
hero = Hero()

# Mount components to activate lifecycle hooks
navbar.mount()
hero.mount()

# Create HTML content
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Snakeskin Landing Page</title>
    <link href="dist/tailwind.css" rel="stylesheet">
</head>
<body>
    {navbar.render()}
    {hero.render()}
</body>
</html>
"""

# Add Bootstrap if needed
# html_content = BootstrapIntegration.include_in_template(html_content, "both")

# Write to file
with open("dist/index.html", "w") as f:
    f.write(html_content)
```

### 4. Run Development Server

```bash
snakeskin dev
```

* The browser will automatically open to `http://localhost:3000/dist`
* Changes to your files will trigger hot reload

### 5. Build Production Version

```bash
snakeskin build
```

* Optimized static files are generated in the `dist` directory
* CSS is minified and assets are optimized

---

## Folder Structure

```
my-landing-page/
├── src/
│   └── components/    # Your UI components
├── dist/              # Build output directory
├── input.css          # Tailwind CSS input file
├── main.py            # Main application entry
├── tailwind.config.js # Tailwind configuration
```

---

## Styling

* **Tailwind CSS**: Fully integrated with automatic processing and hot reload
* **Bootstrap**: Available through the `BootstrapIntegration` helper
* Use CSS classes directly in `render()` for rapid UI design
* See the [Styling Guide](docs/styling_guide.md) for more details

---

## CLI Commands

| Command                                | Description                                    |
| -------------------------------------- | ---------------------------------------------- |
| `snakeskin create <project-name>`      | Scaffold a new project                         |
| `snakeskin dev`                        | Start local development server with hot reload |
| `snakeskin build`                      | Build production-ready static files            |
| `snakeskin deploy <vercel|netlify>`    | Deploy project to Vercel/Netlify               |

---

## Deployment

Snakeskin projects can be deployed to popular hosting platforms:

### Vercel Deployment

```bash
snakeskin deploy vercel
```

See [Vercel Deployment Guide](docs/vercel_deployment.md) for detailed instructions.

### Netlify Deployment

```bash
snakeskin deploy netlify
```

See [Netlify Deployment Guide](docs/netlify_deployment.md) for detailed instructions.

## Future Roadmap

1. **Backend Integration**: REST API / GraphQL / Database support
2. **AI Integration**: Connect components to OpenAI, Gemini, etc.
3. **SSR & Hydration**: Server-side rendering for performance
4. **Plugin System**: Extend framework functionality easily
5. **TypeScript Support**: Type-safe frontend development

---

## Contribution

Snakeskin is **open source** and welcomes contributions!

* Fork the repository
* Create a branch for your feature/fix
* Submit a Pull Request with a detailed description
* Ensure code passes tests and follows style guidelines

---

## License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

## Acknowledgements

Inspired by **React, Vue, Svelte, and Astro**, Snakeskin brings **modern frontend best practices** into a **lightweight, flexible, and developer-friendly framework**.

## Documentation

For more detailed documentation, check out the following guides:

* [Getting Started Guide](docs/getting_started.md)
* [Component Development Guide](docs/component_guide.md)
* [State Management Guide](docs/state_management.md)
* [Styling Guide](docs/styling_guide.md)
* [API Reference](docs/api_reference.md)
* [Troubleshooting Guide](docs/troubleshooting.md)

