class Component:
    """A base class for components in the Mamba framework."""

    def __init__(self,**props):
        self.props = props
        self.state = {}

    def set_state(self, new_state: dict):
        """Update the component's state."""
        self.state.update(new_state)
        self.render()
    
    def render(self):
        """Every component should implement this"""
        raise NotImplementedError("Component must define render() method")