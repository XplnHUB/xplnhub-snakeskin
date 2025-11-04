# Component Development Guide

This guide explains how to create and use components in Snakeskin.

## Component Basics

Components are the building blocks of your Snakeskin application. Each component:

1. Inherits from the `Component` base class
2. Has its own state and props
3. Implements a `render()` method that returns HTML

Here's a basic component:

```python
from snakeskin.framework import Component

class HelloWorld(Component):
    def render(self):
        return """
        <div>
            <h1>Hello, World!</h1>
        </div>
        """
```

## Props

Props are properties passed to a component when it's created:

```python
from snakeskin.framework import Component

class Greeting(Component):
    def render(self):
        name = self.props.get("name", "World")
        return f"""
        <div>
            <h1>Hello, {name}!</h1>
        </div>
        """

# Usage
greeting = Greeting(name="John")
html = greeting.render()  # Renders "Hello, John!"
```

## State Management

Components can maintain internal state that can change over time:

```python
from snakeskin.framework import Component

class Counter(Component):
    def __init__(self, **props):
        super().__init__(**props)
        self.state = {"count": 0}
    
    def increment(self):
        self.set_state({"count": self.state["count"] + 1})
    
    def render(self):
        return f"""
        <div>
            <p>Count: {self.state["count"]}</p>
            <button onclick="increment_{id(self)}()">Increment</button>
            <script>
                function increment_{id(self)}() {{
                    // In a real app, you would use AJAX or WebSockets
                    // to communicate with the server
                    console.log("Increment clicked");
                }}
            </script>
        </div>
        """
```

## Lifecycle Hooks

Snakeskin components have lifecycle hooks that allow you to run code at specific points:

| Hook | Description |
|------|-------------|
| `before_mount` | Called before the component is mounted |
| `mounted` | Called after the component is mounted |
| `before_update` | Called before the component's state is updated |
| `updated` | Called after the component's state is updated |
| `before_unmount` | Called before the component is unmounted |

Example usage:

```python
from snakeskin.framework import Component

class LifecycleDemo(Component):
    def __init__(self, **props):
        super().__init__(**props)
        self.state = {"data": None}
        
        # Register lifecycle hooks
        self.on('mounted', self.load_data)
        self.on('before_unmount', self.cleanup)
    
    def load_data(self, component):
        # Simulate loading data
        print("Loading data...")
        self.set_state({"data": "Loaded data"})
    
    def cleanup(self, component):
        print("Cleaning up resources...")
    
    def render(self):
        data = self.state.get("data", "Loading...")
        return f"""
        <div>
            <p>Data: {data}</p>
        </div>
        """
```

## Event Handling

You can handle events in your components:

```python
from snakeskin.framework import Component

class ClickCounter(Component):
    def __init__(self, **props):
        super().__init__(**props)
        self.state = {"clicks": 0}
    
    def handle_click(self):
        self.set_state({"clicks": self.state["clicks"] + 1})
    
    def render(self):
        return f"""
        <div>
            <p>Clicks: {self.state["clicks"]}</p>
            <button onclick="handleClick_{id(self)}()">Click me</button>
            <script>
                function handleClick_{id(self)}() {{
                    // In a real app, you would use AJAX or WebSockets
                    console.log("Button clicked");
                }}
            </script>
        </div>
        """
```

## Component Composition

You can compose components to build complex UIs:

```python
from snakeskin.framework import Component
from .header import Header
from .sidebar import Sidebar
from .content import Content
from .footer import Footer

class Layout(Component):
    def render(self):
        header = Header(title=self.props.get("title", "My App"))
        sidebar = Sidebar(items=self.props.get("menu_items", []))
        content = Content(content=self.props.get("content", ""))
        footer = Footer(copyright=self.props.get("copyright", "© 2025"))
        
        return f"""
        <div class="layout">
            {header.render()}
            <div class="main">
                {sidebar.render()}
                {content.render()}
            </div>
            {footer.render()}
        </div>
        """
```

## Observers and Reactivity

You can observe state changes in components:

```python
from snakeskin.framework import Component

class ObservableCounter(Component):
    def __init__(self, **props):
        super().__init__(**props)
        self.state = {"count": 0}
        
        # Add an observer to log state changes
        self.observe(self.log_state_change)
    
    def log_state_change(self, state):
        print(f"State changed: {state}")
    
    def increment(self):
        self.set_state({"count": self.state["count"] + 1})
    
    def render(self):
        return f"""
        <div>
            <p>Count: {self.state["count"]}</p>
            <button onclick="increment_{id(self)}()">Increment</button>
            <script>
                function increment_{id(self)}() {{
                    console.log("Increment clicked");
                }}
            </script>
        </div>
        """
```

## Best Practices

1. **Keep components focused**: Each component should do one thing well
2. **Use props for configuration**: Pass configuration through props
3. **Minimize state**: Only keep necessary state in your components
4. **Use lifecycle hooks appropriately**: Clean up resources in `before_unmount`
5. **Document your components**: Add docstrings to explain what each component does

## Advanced Techniques

### Conditional Rendering

```python
def render(self):
    if self.state.get("loading"):
        return """<div class="loading">Loading...</div>"""
    elif self.state.get("error"):
        return f"""<div class="error">{self.state["error"]}</div>"""
    else:
        return f"""<div class="content">{self.state["content"]}</div>"""
```

### List Rendering

```python
def render(self):
    items = self.props.get("items", [])
    items_html = ""
    
    for item in items:
        items_html += f"""
        <li class="item">{item}</li>
        """
    
    return f"""
    <ul class="item-list">
        {items_html}
    </ul>
    """
```

### Component Libraries

You can create reusable component libraries:

```python
# ui_library/button.py
from snakeskin.framework import Component

class Button(Component):
    def render(self):
        variant = self.props.get("variant", "primary")
        size = self.props.get("size", "medium")
        text = self.props.get("text", "Button")
        
        class_map = {
            "primary": "bg-blue-500 hover:bg-blue-700 text-white",
            "secondary": "bg-gray-500 hover:bg-gray-700 text-white",
            "danger": "bg-red-500 hover:bg-red-700 text-white"
        }
        
        size_map = {
            "small": "py-1 px-2 text-sm",
            "medium": "py-2 px-4",
            "large": "py-3 px-6 text-lg"
        }
        
        button_class = f"{class_map.get(variant, class_map['primary'])} {size_map.get(size, size_map['medium'])} font-bold rounded"
        
        return f"""
        <button class="{button_class}">
            {text}
        </button>
        """
```
