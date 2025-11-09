# Getting Started with Snakeskin

Snakeskin is a modern, lightweight frontend framework designed to make building component-based web applications fast, flexible, and enjoyable. This guide will help you get started with Snakeskin.

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

## Creating a New Project

```bash
snakeskin create my-project
cd my-project
```

This will scaffold a new project with the following structure:

```
my-project/
├── src/
│   └── components/    # Your UI components
├── dist/              # Build output directory
├── input.css          # Tailwind CSS input file
├── main.py            # Main application entry
├── tailwind.config.js # Tailwind configuration
```

## Creating Components

Components are the building blocks of your application. Here's how to create a simple component:

```python
# src/components/Button.py
from snakeskin.framework import Component

class Button(Component):
    def __init__(self, **props):
        super().__init__(**props)
        self.state = {
            "clicked": False
        }
        
    def handle_click(self, event=None):
        self.set_state({"clicked": not self.state.get("clicked", False)})
        
    def render(self):
        clicked = self.state.get("clicked", False)
        button_class = "bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
        if clicked:
            button_class = "bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded"
            
        return f"""
        <button 
            class="{button_class}" 
            onclick="handleClick_{id(self)}()"
        >
            {self.props.get("text", "Click me")}
        </button>
        <script>
            function handleClick_{id(self)}() {{
                console.log("Button clicked");
                // In a real application, you would use AJAX or WebSockets to communicate with the server
            }}
        </script>
        """
```

## Using Lifecycle Hooks

Snakeskin provides lifecycle hooks to help you manage component state:

```python
# src/components/Timer.py
from snakeskin.framework import Component
import time

class Timer(Component):
    def __init__(self, **props):
        super().__init__(**props)
        self.state = {
            "seconds": 0
        }
        
        # Register lifecycle hooks
        self.on('mounted', self.start_timer)
        self.on('before_unmount', self.stop_timer)
        
    def start_timer(self, component):
        self.timer_running = True
        # In a real application, you would use a proper timer mechanism
        # This is just for demonstration
        print("Timer started")
        
    def stop_timer(self, component):
        self.timer_running = False
        print("Timer stopped")
        
    def tick(self):
        if self.timer_running:
            self.set_state({"seconds": self.state["seconds"] + 1})
            
    def render(self):
        return f"""
        <div class="timer">
            <p>Seconds elapsed: {self.state["seconds"]}</p>
        </div>
        """
```

## Composing Components

You can compose components to build complex UIs:

```python
# src/components/App.py
from snakeskin.framework import Component
from src.components.Button import Button
from src.components.Timer import Timer

class App(Component):
    def render(self):
        button = Button(text="Toggle Timer")
        timer = Timer()
        
        return f"""
        <div class="container mx-auto p-4">
            <h1 class="text-2xl font-bold mb-4">Snakeskin Demo</h1>
            {button.render()}
            {timer.render()}
        </div>
        """
```

## Running the Development Server

Start the development server with hot reload:

```bash
snakeskin dev
```

This will:
1. Build your project
2. Start a development server at http://localhost:3000
3. Watch for file changes and automatically reload the browser

## Building for Production

When you're ready to deploy:

```bash
snakeskin build
```

This will create optimized files in the `dist` directory that you can deploy to any static hosting service.

## Using Tailwind CSS

Snakeskin integrates seamlessly with Tailwind CSS. You can use Tailwind classes directly in your component's render method:

```python
def render(self):
    return """
    <div class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
        <h2 class="text-gray-700 text-xl font-bold mb-2">Welcome</h2>
        <p class="text-gray-700">This component uses Tailwind CSS for styling.</p>
    </div>
    """
```

## Using Bootstrap

Snakeskin also supports Bootstrap. You can use the BootstrapIntegration helper:

```python
from snakeskin import BootstrapIntegration

# In your main.py
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My App</title>
</head>
<body>
    {app.render()}
</body>
</html>
"""

# Add Bootstrap CSS and JS
html_content = BootstrapIntegration.include_in_template(html_content, "both")

with open("dist/index.html", "w") as f:
    f.write(html_content)
```

Now you can use Bootstrap classes in your components:

```python
def render(self):
    return """
    <div class="container">
        <div class="row">
            <div class="col-md-6">
                <div class="card">
                    <div class="card-body">
                        <h5 class="card-title">Bootstrap Card</h5>
                        <p class="card-text">This component uses Bootstrap for styling.</p>
                        <button class="btn btn-primary">Click me</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """
```

## Next Steps

- Check out the [Component Guide](component_guide.md) for more details on component development
- Learn about [State Management](state_management.md) for managing application state
- Explore [Styling Options](styling_guide.md) for more information on styling your application
- See the [API Reference](api_reference.md) for detailed documentation of all classes and methods
