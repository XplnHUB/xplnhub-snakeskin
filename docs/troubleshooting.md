# Troubleshooting Guide

This guide helps you solve common issues with Snakeskin.

## Installation Issues

### Package Not Found

**Problem**: `pip install snakeskin` fails with "Package not found" error.

**Solution**: 
1. Make sure you're using the correct package name:
   ```bash
   pip install snakeskin
   ```
2. If that doesn't work, try installing from GitHub:
   ```bash
   pip install git+https://github.com/yourusername/snakeskin.git
   ```

### Version Conflicts

**Problem**: Dependencies have version conflicts.

**Solution**:
1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
2. Install Snakeskin in the virtual environment:
   ```bash
   pip install snakeskin
   ```

## CLI Issues

### Command Not Found

**Problem**: `snakeskin` command not found after installation.

**Solution**:
1. Make sure the package is installed:
   ```bash
   pip show snakeskin
   ```
2. Check if the script is in your PATH:
   ```bash
   which snakeskin  # On Windows: where snakeskin
   ```
3. Try reinstalling with:
   ```bash
   pip install --force-reinstall snakeskin
   ```

### Project Creation Fails

**Problem**: `snakeskin create my-project` fails.

**Solution**:
1. Check if the directory already exists and remove it:
   ```bash
   rm -rf my-project
   ```
2. Check permissions:
   ```bash
   mkdir test-dir && rm -rf test-dir
   ```
3. Run with verbose output:
   ```bash
   snakeskin create my-project --verbose
   ```

## Development Server Issues

### Server Won't Start

**Problem**: `snakeskin dev` fails to start the server.

**Solution**:
1. Check if port 3000 is already in use:
   ```bash
   lsof -i :3000  # On Windows: netstat -ano | findstr :3000
   ```
2. Kill the process using that port:
   ```bash
   kill -9 <PID>  # On Windows: taskkill /F /PID <PID>
   ```
3. Try a different port:
   ```bash
   # Edit server.py to use a different port
   # Change PORT = 3000 to PORT = 3001
   ```

### Hot Reload Not Working

**Problem**: Changes to files don't trigger hot reload.

**Solution**:
1. Make sure WebSockets are installed:
   ```bash
   pip install websockets
   ```
2. Check if file watching is working:
   ```bash
   # Create a test file
   touch src/test.py
   ```
3. Restart the development server:
   ```bash
   snakeskin dev
   ```
4. Check browser console for WebSocket errors

## Tailwind CSS Issues

### Tailwind Classes Not Applied

**Problem**: Tailwind CSS classes are not being applied to elements.

**Solution**:
1. Check if Tailwind CSS is being built:
   ```bash
   ls -la dist/tailwind.css
   ```
2. Make sure the CSS file is included in your HTML:
   ```html
   <link href="tailwind.css" rel="stylesheet">
   ```
3. Check if your HTML elements have the correct classes:
   ```html
   <div class="bg-blue-500">This should be blue</div>
   ```
4. Rebuild Tailwind CSS manually:
   ```bash
   npx tailwindcss -i ./input.css -o ./dist/tailwind.css
   ```

### Custom Tailwind Configuration Not Working

**Problem**: Custom Tailwind configuration is not being applied.

**Solution**:
1. Check your `tailwind.config.js` file:
   ```javascript
   module.exports = {
     content: ["./src/components/**/*.py", "./main.py"],
     theme: {
       extend: {
         // Your custom configuration
       },
     },
     plugins: [],
   };
   ```
2. Make sure the content paths are correct
3. Rebuild Tailwind CSS:
   ```bash
   npx tailwindcss -i ./input.css -o ./dist/tailwind.css
   ```

## Bootstrap Issues

### Bootstrap Styles Not Applied

**Problem**: Bootstrap styles are not being applied.

**Solution**:
1. Check if Bootstrap is included in your HTML:
   ```html
   <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
   <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
   ```
2. Use the `BootstrapIntegration` helper:
   ```python
   from snakeskin import BootstrapIntegration
   
   html_content = """<!DOCTYPE html><html>...</html>"""
   html_content = BootstrapIntegration.include_in_template(html_content, "both")
   ```

### Bootstrap JavaScript Not Working

**Problem**: Bootstrap JavaScript components (dropdowns, modals, etc.) don't work.

**Solution**:
1. Make sure the Bootstrap JavaScript is included:
   ```html
   <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
   ```
2. Initialize Bootstrap components manually:
   ```html
   <script>
     document.addEventListener('DOMContentLoaded', function() {
       // Initialize all tooltips
       var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
       var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
         return new bootstrap.Tooltip(tooltipTriggerEl)
       })
     });
   </script>
   ```

## Component Issues

### Component Not Rendering

**Problem**: Component is not rendering or renders incorrectly.

**Solution**:
1. Check if the `render()` method is implemented:
   ```python
   def render(self):
       return "<div>My Component</div>"
   ```
2. Check for syntax errors in the HTML string:
   ```python
   def render(self):
       # Correct
       return """
       <div>
           <h1>Title</h1>
           <p>Content</p>
       </div>
       """
   ```
3. Print the rendered HTML for debugging:
   ```python
   html = component.render()
   print(html)
   ```

### State Updates Not Working

**Problem**: Component state updates don't trigger re-renders.

**Solution**:
1. Make sure you're using `set_state()` to update state:
   ```python
   # Correct
   self.set_state({"count": self.state["count"] + 1})
   
   # Incorrect
   self.state["count"] += 1
   ```
2. Check if observers are registered:
   ```python
   def __init__(self, **props):
       super().__init__(**props)
       self.observe(self.on_state_change)
   
   def on_state_change(self, state):
       print(f"State changed: {state}")
   ```

## Build Issues

### Build Fails

**Problem**: `snakeskin build` fails.

**Solution**:
1. Check for errors in your components:
   ```bash
   python -m py_compile src/components/*.py
   ```
2. Check if `main.py` exists and is correct:
   ```bash
   python -m py_compile main.py
   ```
3. Run with verbose output:
   ```bash
   snakeskin build --verbose
   ```

### Missing Files in Build

**Problem**: Some files are missing in the build output.

**Solution**:
1. Check if all files are being copied:
   ```python
   # In utils.py, add logging
   print(f"Copying {src} to {dest}")
   ```
2. Manually copy missing files:
   ```bash
   cp src/assets/* dist/assets/
   ```

## Common Error Messages

### "No module named 'snakeskin'"

**Problem**: Python can't find the snakeskin module.

**Solution**:
1. Check if the package is installed:
   ```bash
   pip show snakeskin
   ```
2. Check your import statements:
   ```python
   # Correct
   from snakeskin.framework import Component
   ```

### "Component must define render() method"

**Problem**: You're using a component that doesn't have a render method.

**Solution**:
1. Implement the `render()` method:
   ```python
   class MyComponent(Component):
       def render(self):
           return "<div>My Component</div>"
   ```

### "TypeError: 'NoneType' object is not callable"

**Problem**: You're trying to call a method that doesn't exist.

**Solution**:
1. Check if the method exists:
   ```python
   # Check if on_click is a callable function
   on_click = self.props.get("on_click")
   if callable(on_click):
       on_click()
   ```

## Advanced Troubleshooting

### Debugging Components

```python
class DebugComponent(Component):
    def __init__(self, **props):
        super().__init__(**props)
        self.debug = props.get("debug", False)
    
    def log(self, message):
        if self.debug:
            print(f"[DEBUG] {self.__class__.__name__}: {message}")
    
    def set_state(self, new_state):
        self.log(f"State update: {new_state}")
        return super().set_state(new_state)
    
    def render(self):
        self.log("Rendering component")
        html = "<div>Debug Component</div>"
        self.log(f"Rendered HTML: {html}")
        return html
```

### Performance Issues

If your application is slow:

1. Minimize state updates
2. Use smaller components
3. Avoid deep nesting of components
4. Profile your Python code:
   ```bash
   python -m cProfile -o profile.pstats main.py
   ```
5. Analyze the profile:
   ```bash
   python -c "import pstats; p = pstats.Stats('profile.pstats'); p.sort_stats('cumulative').print_stats(30)"
   ```

## Getting Help

If you're still having issues:

1. Check the [GitHub repository](https://github.com/yourusername/snakeskin) for known issues
2. Join the community Discord server
3. Open an issue on GitHub with:
   - A minimal reproducible example
   - Your environment information
   - Error messages and logs
