# API Reference

This document provides detailed information about the Snakeskin API.

## Component Class

The `Component` class is the core building block of Snakeskin applications.

### Constructor

```python
Component(**props)
```

**Parameters:**
- `props`: A dictionary of properties passed to the component

**Example:**
```python
from snakeskin.framework import Component

# Create a component with props
my_component = Component(title="Hello", subtitle="World")
```

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `props` | `dict` | Properties passed to the component |
| `state` | `dict` | Internal state of the component |
| `_observers` | `list` | List of observer callbacks |
| `_mounted` | `bool` | Whether the component is mounted |
| `_lifecycle_hooks` | `dict` | Dictionary of lifecycle hook callbacks |

### Methods

#### `set_state(new_state: dict) -> str`

Updates the component's state and triggers a re-render.

**Parameters:**
- `new_state`: A dictionary of state values to update

**Returns:**
- The rendered HTML as a string

**Example:**
```python
component.set_state({"count": 42})
```

#### `mount() -> str`

Mounts the component and triggers the 'mounted' lifecycle hook.

**Returns:**
- The rendered HTML as a string

**Example:**
```python
html = component.mount()
```

#### `unmount() -> None`

Unmounts the component and triggers the 'before_unmount' lifecycle hook.

**Example:**
```python
component.unmount()
```

#### `observe(callback: callable) -> int`

Adds an observer callback that will be called when the state changes.

**Parameters:**
- `callback`: A function that takes the state as a parameter

**Returns:**
- An observer ID that can be used to remove the observer

**Example:**
```python
def log_state(state):
    print(f"State changed: {state}")

observer_id = component.observe(log_state)
```

#### `unobserve(observer_id: int) -> None`

Removes an observer callback.

**Parameters:**
- `observer_id`: The ID returned by the `observe` method

**Example:**
```python
component.unobserve(observer_id)
```

#### `on(event: str, callback: callable) -> None`

Registers a callback for a lifecycle event.

**Parameters:**
- `event`: The name of the event ('before_mount', 'mounted', 'before_update', 'updated', 'before_unmount')
- `callback`: A function that takes the component as a parameter

**Example:**
```python
def on_mounted(component):
    print("Component mounted")

component.on('mounted', on_mounted)
```

#### `render() -> str`

Renders the component to HTML. This method must be implemented by subclasses.

**Returns:**
- The rendered HTML as a string

**Example:**
```python
class MyComponent(Component):
    def render(self):
        return "<div>Hello, World!</div>"
```

## TailwindIntegration Class

The `TailwindIntegration` class provides helpers for Tailwind CSS integration.

### Static Methods

#### `setup(project_path: str) -> None`

Sets up Tailwind CSS in a project.

**Parameters:**
- `project_path`: The path to the project directory

**Example:**
```python
from snakeskin import TailwindIntegration

TailwindIntegration.setup("./my-project")
```

#### `build(output_path: str = "./dist/tailwind.css", minify: bool = True) -> None`

Builds Tailwind CSS.

**Parameters:**
- `output_path`: The path where the CSS file will be written
- `minify`: Whether to minify the CSS

**Example:**
```python
TailwindIntegration.build("./dist/styles.css", minify=True)
```

## BootstrapIntegration Class

The `BootstrapIntegration` class provides helpers for Bootstrap integration.

### Static Methods

#### `setup(project_path: str) -> None`

Sets up Bootstrap in a project.

**Parameters:**
- `project_path`: The path to the project directory

**Example:**
```python
from snakeskin import BootstrapIntegration

BootstrapIntegration.setup("./my-project")
```

#### `get_cdn_links() -> dict`

Gets Bootstrap CDN links for CSS and JS.

**Returns:**
- A dictionary with 'css' and 'js' keys containing the HTML tags

**Example:**
```python
links = BootstrapIntegration.get_cdn_links()
css_link = links['css']
js_script = links['js']
```

#### `include_in_template(template: str, position: str = "head") -> str`

Includes Bootstrap in an HTML template.

**Parameters:**
- `template`: The HTML template
- `position`: Where to include Bootstrap ('head', 'body', or 'both')

**Returns:**
- The modified HTML template

**Example:**
```python
html = """
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

bootstrap_html = BootstrapIntegration.include_in_template(html, "both")
```

## CLI Commands

Snakeskin provides several CLI commands for project management.

### `snakeskin create <project-name>`

Creates a new Snakeskin project.

**Parameters:**
- `project-name`: The name of the project to create

**Example:**
```bash
snakeskin create my-project
```

### `snakeskin dev`

Starts the development server with hot reload.

**Example:**
```bash
snakeskin dev
```

### `snakeskin build`

Builds the project for production.

**Example:**
```bash
snakeskin build
```

## Lifecycle Hooks

Snakeskin components have several lifecycle hooks:

| Hook | Description |
|------|-------------|
| `before_mount` | Called before the component is mounted |
| `mounted` | Called after the component is mounted |
| `before_update` | Called before the component's state is updated |
| `updated` | Called after the component's state is updated |
| `before_unmount` | Called before the component is unmounted |

**Example:**
```python
from snakeskin.framework import Component

class LifecycleComponent(Component):
    def __init__(self, **props):
        super().__init__(**props)
        
        # Register lifecycle hooks
        self.on('before_mount', self.on_before_mount)
        self.on('mounted', self.on_mounted)
        self.on('before_update', self.on_before_update)
        self.on('updated', self.on_updated)
        self.on('before_unmount', self.on_before_unmount)
    
    def on_before_mount(self, component):
        print("Before mount")
    
    def on_mounted(self, component):
        print("Mounted")
    
    def on_before_update(self, component):
        print("Before update")
    
    def on_updated(self, component):
        print("Updated")
    
    def on_before_unmount(self, component):
        print("Before unmount")
    
    def render(self):
        return "<div>Lifecycle Component</div>"
```

## Error Handling

Snakeskin provides several ways to handle errors:

### Component Error Handling

```python
from snakeskin.framework import Component

class ErrorHandlingComponent(Component):
    def __init__(self, **props):
        super().__init__(**props)
        self.state = {"error": None, "data": None}
    
    def fetch_data(self):
        try:
            # Simulate API call
            data = {"name": "Example"}
            self.set_state({"data": data, "error": None})
        except Exception as e:
            self.set_state({"error": str(e), "data": None})
    
    def render(self):
        if self.state.get("error"):
            return f"""
            <div class="error">
                <h2>Error</h2>
                <p>{self.state["error"]}</p>
            </div>
            """
        elif self.state.get("data"):
            return f"""
            <div class="data">
                <h2>Data</h2>
                <p>{self.state["data"]["name"]}</p>
            </div>
            """
        else:
            return """
            <div class="loading">
                <p>Loading...</p>
            </div>
            """
```

### Global Error Handling

You can implement a global error handler for your application:

```python
# error_handler.py
class ErrorHandler:
    def __init__(self):
        self.errors = []
        self.error_callbacks = []
    
    def capture_error(self, error, component=None):
        error_info = {
            "error": error,
            "component": component.__class__.__name__ if component else None,
            "timestamp": time.time()
        }
        self.errors.append(error_info)
        self._notify_callbacks(error_info)
        
        # Log the error
        print(f"Error in {error_info['component']}: {error}")
    
    def add_callback(self, callback):
        self.error_callbacks.append(callback)
    
    def _notify_callbacks(self, error_info):
        for callback in self.error_callbacks:
            callback(error_info)

# Create a singleton instance
error_handler = ErrorHandler()
```

```python
# In your component
from error_handler import error_handler

class ComponentWithErrorHandling(Component):
    def risky_operation(self):
        try:
            # Some risky operation
            result = 1 / 0  # Will raise ZeroDivisionError
            return result
        except Exception as e:
            error_handler.capture_error(e, self)
            return None
```

## Troubleshooting

For common issues and their solutions, see the [Troubleshooting Guide](troubleshooting.md).
