# State Management Guide

This guide explains how to manage state in your Snakeskin applications.

## Component State Basics

Each Snakeskin component can maintain its own internal state. State is a dictionary of values that can change over time and trigger re-renders.

```python
from snakeskin.framework import Component

class Counter(Component):
    def __init__(self, **props):
        super().__init__(**props)
        # Initialize state
        self.state = {"count": 0}
    
    def increment(self):
        # Update state
        self.set_state({"count": self.state["count"] + 1})
    
    def render(self):
        return f"""
        <div>
            <p>Count: {self.state["count"]}</p>
            <button onclick="increment_{id(self)}()">Increment</button>
            <script>
                function increment_{id(self)}() {{
                    // In a real app, you would use AJAX or WebSockets
                    console.log("Increment clicked");
                }}
            </script>
        </div>
        """
```

## The `set_state` Method

The `set_state` method is the primary way to update a component's state:

1. It merges the new state with the existing state
2. It triggers the component's `before_update` lifecycle hook
3. It notifies all observers of the state change
4. It triggers the component's `updated` lifecycle hook
5. It returns the result of calling the component's `render` method

```python
def set_state(self, new_state: dict):
    # Call lifecycle hook
    self._call_hooks('before_update')
    
    # Update state
    self.state.update(new_state)
    
    # Notify observers
    for observer in self._observers:
        observer(self.state)
        
    # Call lifecycle hook
    self._call_hooks('updated')
    
    # Re-render
    return self.render()
```

## Reactive State with Observers

Snakeskin provides an observer pattern for reactive state management. You can register observers that will be notified whenever the state changes:

```python
from snakeskin.framework import Component

class ObservableCounter(Component):
    def __init__(self, **props):
        super().__init__(**props)
        self.state = {"count": 0}
        
        # Add an observer to log state changes
        self.observer_id = self.observe(self.log_state_change)
    
    def log_state_change(self, state):
        print(f"State changed: {state}")
    
    def increment(self):
        self.set_state({"count": self.state["count"] + 1})
    
    def cleanup(self):
        # Remove the observer when no longer needed
        self.unobserve(self.observer_id)
    
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

## Lifecycle Hooks and State

Lifecycle hooks provide a way to respond to state changes:

```python
from snakeskin.framework import Component

class DataFetcher(Component):
    def __init__(self, **props):
        super().__init__(**props)
        self.state = {
            "loading": True,
            "data": None,
            "error": None
        }
        
        # Register lifecycle hooks
        self.on('mounted', self.fetch_data)
        self.on('updated', self.log_update)
    
    def fetch_data(self, component):
        # Simulate fetching data
        try:
            # In a real app, this would be an API call
            data = {"name": "Example", "value": 42}
            self.set_state({"loading": False, "data": data})
        except Exception as e:
            self.set_state({"loading": False, "error": str(e)})
    
    def log_update(self, component):
        print(f"Component updated with state: {self.state}")
    
    def render(self):
        if self.state["loading"]:
            return """<div>Loading...</div>"""
        elif self.state["error"]:
            return f"""<div>Error: {self.state["error"]}</div>"""
        else:
            return f"""
            <div>
                <h2>{self.state["data"]["name"]}</h2>
                <p>Value: {self.state["data"]["value"]}</p>
            </div>
            """
```

## Sharing State Between Components

There are several ways to share state between components:

### 1. Props Passing

Pass state from parent to child components through props:

```python
from snakeskin.framework import Component
from .child import ChildComponent

class ParentComponent(Component):
    def __init__(self, **props):
        super().__init__(**props)
        self.state = {"shared_value": 42}
    
    def render(self):
        # Pass state as props to child component
        child = ChildComponent(value=self.state["shared_value"])
        return f"""
        <div>
            <h2>Parent Component</h2>
            <p>Value: {self.state["shared_value"]}</p>
            {child.render()}
        </div>
        """
```

### 2. Callback Functions

Pass callback functions to allow child components to update parent state:

```python
from snakeskin.framework import Component
from .child_with_callback import ChildWithCallback

class ParentWithCallback(Component):
    def __init__(self, **props):
        super().__init__(**props)
        self.state = {"shared_value": 42}
    
    def update_value(self, new_value):
        self.set_state({"shared_value": new_value})
    
    def render(self):
        # Pass state and callback to child component
        child = ChildWithCallback(
            value=self.state["shared_value"],
            on_change=self.update_value
        )
        return f"""
        <div>
            <h2>Parent Component</h2>
            <p>Value: {self.state["shared_value"]}</p>
            {child.render()}
        </div>
        """
```

```python
# child_with_callback.py
from snakeskin.framework import Component

class ChildWithCallback(Component):
    def increment(self):
        # Call the parent's callback function
        current_value = self.props.get("value", 0)
        on_change = self.props.get("on_change")
        if on_change:
            on_change(current_value + 1)
    
    def render(self):
        value = self.props.get("value", 0)
        return f"""
        <div>
            <h3>Child Component</h3>
            <p>Value: {value}</p>
            <button onclick="increment_{id(self)}()">Increment</button>
            <script>
                function increment_{id(self)}() {{
                    console.log("Child increment clicked");
                }}
            </script>
        </div>
        """
```

### 3. Global State

For more complex applications, you can implement a simple global state manager:

```python
# state_manager.py
class StateManager:
    def __init__(self):
        self.state = {}
        self.observers = []
    
    def get_state(self):
        return self.state.copy()
    
    def set_state(self, new_state):
        self.state.update(new_state)
        self._notify_observers()
    
    def observe(self, callback):
        self.observers.append(callback)
        return len(self.observers) - 1
    
    def unobserve(self, observer_id):
        if 0 <= observer_id < len(self.observers):
            self.observers.pop(observer_id)
    
    def _notify_observers(self):
        for observer in self.observers:
            observer(self.state)

# Create a singleton instance
global_state = StateManager()
```

```python
# component_with_global_state.py
from snakeskin.framework import Component
from .state_manager import global_state

class GlobalStateComponent(Component):
    def __init__(self, **props):
        super().__init__(**props)
        self.state = {"local_value": 0}
        
        # Observe global state
        self.global_observer_id = global_state.observe(self.on_global_state_change)
        
        # Register cleanup
        self.on('before_unmount', self.cleanup)
    
    def on_global_state_change(self, global_state_data):
        # Update local state based on global state
        self.set_state({"local_value": global_state_data.get("counter", 0)})
    
    def increment_global(self):
        current = global_state.get_state().get("counter", 0)
        global_state.set_state({"counter": current + 1})
    
    def cleanup(self, component):
        # Clean up global state observer
        global_state.unobserve(self.global_observer_id)
    
    def render(self):
        return f"""
        <div>
            <h3>Global State Component</h3>
            <p>Local value: {self.state["local_value"]}</p>
            <button onclick="incrementGlobal_{id(self)}()">Increment Global</button>
            <script>
                function incrementGlobal_{id(self)}() {{
                    console.log("Increment global clicked");
                }}
            </script>
        </div>
        """
```

## Best Practices for State Management

1. **Keep state minimal**: Only store what you need in state
2. **Use props for configuration**: Pass configuration through props
3. **Lift state up**: Move shared state to the nearest common ancestor
4. **Use callbacks for child-to-parent communication**
5. **Consider global state only when necessary**
6. **Clean up observers**: Always remove observers when components are unmounted
7. **Use immutable patterns**: Treat state as immutable and create new objects when updating
8. **Document state shape**: Add comments describing the expected state structure
