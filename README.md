# Mamba

Mamba is a **modern, lightweight frontend framework/library** designed to make building **component-based web applications** fast, flexible, and enjoyable. It integrates seamlessly with **Tailwind CSS** and **Bootstrap**, and provides a **CLI tool** to scaffold, run, and build projects effortlessly. Mamba is designed to be **AI-ready and backend-friendly** for future integrations.

---

## Features

- **Component-Based Architecture**: Build reusable UI components easily.  
- **State Management**: Reactive state system with lifecycle hooks.  
- **Tailwind CSS & Bootstrap Integration**: Style your apps with your favorite frameworks.  
- **CLI Tooling**:
  - `mamba create <project-name>` → Scaffold a new project  
  - `mamba dev` → Start a local development server with hot reload  
  - `mamba build` → Generate production-ready build  
- **Fast Development & Deployment**: Optimized build system and CLI for Vercel/Netlify deployments.  
- **Future-Ready**: Planned support for backend integrations, AI models, and databases.  

---

## Installation

```bash
pip install mamba
````

> **Note**: Mamba is written in Python and provides a lightweight frontend runtime. Future versions may include a full JS/TS runtime for advanced features.

---

## Quick Start

### 1. Create a New Project

```bash
mamba create my-landing-page
cd my-landing-page
```

### 2. Add Components

```python
# src/components/Hero.py
from framework import Component

class Hero(Component):
    def render(self):
        return """
        <section class="text-center py-20 bg-gray-100">
            <h1 class="text-5xl font-bold mb-4">Welcome to Mamba</h1>
            <p class="text-gray-600 mb-6">Build modern web apps effortlessly.</p>
            <button class="bg-blue-500 text-white px-6 py-3 rounded hover:bg-blue-600">
                Get Started
            </button>
        </section>
        """
```

### 3. Compose Components

```python
# main.py
from src.components.Navbar import Navbar
from src.components.Hero import Hero

navbar = Navbar()
hero = Hero()

html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Mamba Landing Page</title>
    <link href="tailwind.css" rel="stylesheet">
</head>
<body>
    {navbar.render()}
    {hero.render()}
</body>
</html>
"""

with open("index.html", "w") as f:
    f.write(html_content)
```

### 4. Run Development Server

```bash
mamba dev
```

* Open `http://localhost:3000` to see live updates.

### 5. Build Production Version

```bash
mamba build
```

* Optimized static files are ready for deployment.

---

## Folder Structure

```
my-landing-page/
├── src/
│   └── components/    # Your UI components
├── index.html          # Entry HTML file
├── main.py             # Main application entry
├── tailwind.config.js  # Tailwind configuration
├── mamba.json          # Project metadata & config
```

---

## Styling

* Tailwind CSS and Bootstrap fully supported.
* Use CSS classes directly in `render()` for rapid UI design.

---

## 🔧 CLI Commands

| Command                       | Description                                    |
| ----------------------------- | ---------------------------------------------- |
| `mamba create <project-name>` | Scaffold a new project                         |
| `mamba dev`                   | Start local development server with hot reload |
| `mamba build`                 | Build production-ready static files            |
| `mamba deploy` *(future)*     | Deploy project to Vercel/Netlify               |

---

## 🌐 Future Roadmap

1. **Backend Integration**: REST API / GraphQL / Database support
2. **AI Integration**: Connect components to OpenAI, Gemini, etc.
3. **SSR & Hydration**: Server-side rendering for performance
4. **Plugin System**: Extend framework functionality easily
5. **TypeScript Support**: Type-safe frontend development

---

## Contribution

Mamba is **open source** and welcomes contributions!

* Fork the repository
* Create a branch for your feature/fix
* Submit a Pull Request with a detailed description
* Ensure code passes tests and follows style guidelines

---

## License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

## Acknowledgements

Inspired by **React, Vue, Svelte, and Astro**, Mamba brings **modern frontend best practices** into a **lightweight, flexible, and developer-friendly framework**.

