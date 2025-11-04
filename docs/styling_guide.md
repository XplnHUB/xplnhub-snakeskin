# Styling Guide

This guide explains how to style your Snakeskin applications using Tailwind CSS and Bootstrap.

## Tailwind CSS Integration

Snakeskin comes with built-in Tailwind CSS support. Here's how to use it:

### Setup

When you create a new project with `snakeskin create`, Tailwind CSS is automatically set up with:

1. A `tailwind.config.js` file for configuration
2. An `input.css` file with the basic Tailwind directives
3. Build process integration to generate the final CSS

### Using Tailwind Classes

You can use Tailwind classes directly in your component's render method:

```python
from snakeskin.framework import Component

class TailwindCard(Component):
    def render(self):
        return f"""
        <div class="max-w-md mx-auto bg-white rounded-xl shadow-md overflow-hidden md:max-w-2xl m-4">
            <div class="md:flex">
                <div class="md:shrink-0">
                    <img class="h-48 w-full object-cover md:h-full md:w-48" 
                         src="{self.props.get('image_url', 'https://via.placeholder.com/150')}" 
                         alt="Card image">
                </div>
                <div class="p-8">
                    <div class="uppercase tracking-wide text-sm text-indigo-500 font-semibold">
                        {self.props.get('category', 'Category')}
                    </div>
                    <a href="#" class="block mt-1 text-lg leading-tight font-medium text-black hover:underline">
                        {self.props.get('title', 'Title')}
                    </a>
                    <p class="mt-2 text-gray-500">
                        {self.props.get('description', 'Description')}
                    </p>
                </div>
            </div>
        </div>
        """
```

### Customizing Tailwind

You can customize Tailwind by editing the `tailwind.config.js` file:

```javascript
module.exports = {
  content: ["./src/components/**/*.py", "./main.py"],
  theme: {
    extend: {
      colors: {
        'brand-primary': '#3490dc',
        'brand-secondary': '#ffed4a',
        'brand-danger': '#e3342f',
      },
      fontFamily: {
        sans: ['Graphik', 'sans-serif'],
        serif: ['Merriweather', 'serif'],
      },
    },
  },
  plugins: [],
};
```

### Using the TailwindIntegration Helper

Snakeskin provides a `TailwindIntegration` helper class:

```python
from snakeskin import TailwindIntegration

# Set up Tailwind in a project
TailwindIntegration.setup("./my-project")

# Build Tailwind CSS
TailwindIntegration.build("./dist/styles.css", minify=True)
```

## Bootstrap Integration

Snakeskin also supports Bootstrap for styling:

### Setup

To use Bootstrap, you can use the `BootstrapIntegration` helper:

```python
from snakeskin import BootstrapIntegration

# Set up Bootstrap in a project
BootstrapIntegration.setup("./my-project")

# Get Bootstrap CDN links
links = BootstrapIntegration.get_cdn_links()
print(links['css'])  # CSS link tag
print(links['js'])   # JS script tag

# Include Bootstrap in an HTML template
html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>My App</title>
</head>
<body>
    <div id="app"></div>
</body>
</html>
"""

# Add both CSS and JS
bootstrap_html = BootstrapIntegration.include_in_template(html_template, "both")
```

### Using Bootstrap Classes

You can use Bootstrap classes directly in your component's render method:

```python
from snakeskin.framework import Component

class BootstrapCard(Component):
    def render(self):
        return f"""
        <div class="card" style="width: 18rem;">
            <img src="{self.props.get('image_url', 'https://via.placeholder.com/150')}" 
                 class="card-img-top" alt="Card image">
            <div class="card-body">
                <h5 class="card-title">{self.props.get('title', 'Card title')}</h5>
                <p class="card-text">{self.props.get('description', 'Some quick example text.')}</p>
                <a href="#" class="btn btn-primary">Go somewhere</a>
            </div>
        </div>
        """
```

### Bootstrap Components

Bootstrap provides many components that you can use in your Snakeskin components:

```python
from snakeskin.framework import Component

class BootstrapNavbar(Component):
    def render(self):
        return """
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <div class="container-fluid">
                <a class="navbar-brand" href="#">Navbar</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" 
                        data-bs-target="#navbarNav" aria-controls="navbarNav" 
                        aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarNav">
                    <ul class="navbar-nav">
                        <li class="nav-item">
                            <a class="nav-link active" aria-current="page" href="#">Home</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#">Features</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#">Pricing</a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
        """
```

## Combining Tailwind CSS and Bootstrap

You can use both Tailwind CSS and Bootstrap in the same project, but be careful about class name conflicts. Here's how to combine them:

```python
from snakeskin.framework import Component
from snakeskin import BootstrapIntegration

class HybridComponent(Component):
    def render(self):
        return """
        <!-- Bootstrap grid -->
        <div class="container">
            <div class="row">
                <div class="col-md-6">
                    <!-- Tailwind styled content -->
                    <div class="bg-blue-500 text-white p-4 rounded shadow-lg">
                        <h2 class="text-xl font-bold">Tailwind Section</h2>
                        <p class="mt-2">This section uses Tailwind classes.</p>
                    </div>
                </div>
                <div class="col-md-6">
                    <!-- Bootstrap styled content -->
                    <div class="card">
                        <div class="card-body">
                            <h5 class="card-title">Bootstrap Section</h5>
                            <p class="card-text">This section uses Bootstrap classes.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        """

# In main.py
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Hybrid Styling</title>
    <link href="tailwind.css" rel="stylesheet">
</head>
<body>
    {app.render()}
</body>
</html>
"""

# Add Bootstrap
html_content = BootstrapIntegration.include_in_template(html_content, "both")
```

## Custom CSS

You can also include custom CSS in your Snakeskin applications:

### Inline Styles

```python
def render(self):
    return f"""
    <div style="color: blue; font-size: 18px; margin: 20px;">
        This has inline styles.
    </div>
    """
```

### Custom CSS Files

1. Create a CSS file in your project:

```css
/* src/styles/custom.css */
.custom-component {
    border: 1px solid #ccc;
    padding: 15px;
    border-radius: 5px;
    background-color: #f9f9f9;
}

.custom-component h2 {
    color: #333;
    border-bottom: 1px solid #eee;
    padding-bottom: 10px;
}
```

2. Include it in your HTML template:

```python
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>My App</title>
    <link href="tailwind.css" rel="stylesheet">
    <link href="styles/custom.css" rel="stylesheet">
</head>
<body>
    {app.render()}
</body>
</html>
"""
```

3. Use the custom classes in your components:

```python
def render(self):
    return """
    <div class="custom-component">
        <h2>Custom Styled Component</h2>
        <p>This uses custom CSS classes.</p>
    </div>
    """
```

## Best Practices

1. **Choose one primary styling approach**: Either Tailwind CSS or Bootstrap as your main styling system
2. **Use utility classes for one-off styling**: Tailwind is great for this
3. **Use component classes for reusable patterns**: Create custom CSS for reusable patterns
4. **Be consistent**: Stick to a consistent naming convention
5. **Organize styles**: Keep styles organized by component or feature
6. **Avoid inline styles**: Use classes whenever possible for better maintainability
7. **Consider responsive design**: Use responsive utility classes from Tailwind or Bootstrap
8. **Document your styling conventions**: Create a style guide for your project
