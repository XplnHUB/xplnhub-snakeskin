class Component:
    """A base class for components in the Snakeskin framework."""

    def __init__(self, **props):
        self.props = props
        self.state = {}
        self._observers = []
        self._mounted = False
        self._lifecycle_hooks = {
            'before_mount': [],
            'mounted': [],
            'before_update': [],
            'updated': [],
            'before_unmount': []
        }
        # Call lifecycle hook
        self._call_hooks('before_mount')

    def set_state(self, new_state: dict):
        """Update the component's state with reactivity."""
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
    
    def mount(self):
        """Mount the component."""
        if not self._mounted:
            self._mounted = True
            self._call_hooks('mounted')
        return self.render()
    
    def unmount(self):
        """Unmount the component."""
        self._call_hooks('before_unmount')
        self._mounted = False
        self._observers = []
    
    def observe(self, callback):
        """Add an observer to the component's state."""
        self._observers.append(callback)
        return len(self._observers) - 1
    
    def unobserve(self, observer_id):
        """Remove an observer from the component's state."""
        if 0 <= observer_id < len(self._observers):
            self._observers.pop(observer_id)
    
    def on(self, event, callback):
        """Add a lifecycle hook."""
        if event in self._lifecycle_hooks:
            self._lifecycle_hooks[event].append(callback)
    
    def _call_hooks(self, event):
        """Call all registered callbacks for a lifecycle event."""
        if event in self._lifecycle_hooks:
            for callback in self._lifecycle_hooks[event]:
                callback(self)
    
    def render(self):
        """Every component should implement this"""
        raise NotImplementedError("Component must define render() method")