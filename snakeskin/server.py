import http.server
import socketserver
import os
import threading
import subprocess
import time
import webbrowser
import signal
import sys
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

PORT = 3000  # Changed to match README

class HotReloadHandler(FileSystemEventHandler):
    """File system event handler for hot reload."""
    
    def __init__(self, callback):
        self.callback = callback
        self.last_modified = time.time()
    
    def on_modified(self, event):
        # Debounce events (prevent multiple reloads for the same change)
        if time.time() - self.last_modified < 0.5:
            return
        
        self.last_modified = time.time()
        if event.is_directory:
            return
            
        # Only reload for Python files and HTML/CSS files
        if event.src_path.endswith(('.py', '.html', '.css')):
            print(f"File changed: {event.src_path}")
            self.callback()


def inject_hot_reload_script(html_file):
    """Inject hot reload script into HTML file."""
    with open(html_file, 'r') as f:
        content = f.read()
    
    # Add hot reload script before closing body tag
    hot_reload_script = """
    <script>
        // Hot reload script
        const socket = new WebSocket(`ws://${window.location.hostname}:${parseInt(window.location.port) + 1}`);
        socket.onmessage = function(event) {
            if (event.data === 'reload') {
                console.log('Hot reload triggered');
                window.location.reload();
            }
        };
        socket.onclose = function() {
            console.log('Hot reload connection closed. Attempting to reconnect...');
            setTimeout(() => {
                window.location.reload();
            }, 2000);
        };
    </script>
    """
    
    if '</body>' in content:
        content = content.replace('</body>', f"{hot_reload_script}\n</body>")
    else:
        content += hot_reload_script
    
    with open(html_file, 'w') as f:
        f.write(content)


class WebSocketReloadServer(threading.Thread):
    """WebSocket server for hot reload."""
    
    def __init__(self, port):
        threading.Thread.__init__(self)
        self.port = port
        self.daemon = True
        self.connections = []
        self.server = None
        
    def run(self):
        try:
            import websockets
            import asyncio
            
            async def handler(websocket, path):
                self.connections.append(websocket)
                try:
                    await websocket.wait_closed()
                finally:
                    self.connections.remove(websocket)
            
            async def serve():
                self.server = await websockets.serve(handler, "localhost", self.port)
                await self.server.wait_closed()
            
            asyncio.run(serve())
        except ImportError:
            print("WebSockets not available. Hot reload disabled.")
            print("Install with: pip install websockets")
    
    def trigger_reload(self):
        """Trigger reload for all connected clients."""
        if not self.connections:
            return
            
        import asyncio
        
        async def send_reload():
            for conn in list(self.connections):
                try:
                    await conn.send("reload")
                except:
                    pass
        
        asyncio.run(send_reload())


def run_tailwind_watch():
    """Start Tailwind CSS process if config exists"""
    if os.path.exists("tailwind.config.js"):
        try:
            process = subprocess.Popen(
                ["npx", "tailwindcss", "-i", "./input.css", "-o", "./dist/tailwind.css", "--watch"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            print("Tailwind CSS is watching for changes...")
            return process
        except FileNotFoundError:
            print("Tailwind CSS is not installed. Please install it to use this feature.")
    else:
        print("No Tailwind CSS configuration found. Skipping Tailwind watch.")
    return None


def rebuild_project():
    """Rebuild the project when files change."""
    print("\n🔄 Rebuilding project...")
    try:
        result = subprocess.run(
            ["python", "main.py"],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            print("✅ Build successful")
            return True
        else:
            print("❌ Build failed:")
            print(result.stderr)
            return False
    except Exception as e:
        print(f"❌ Build error: {e}")
        return False


def run_dev_server():
    """Run the local dev server with hot reload"""
    # Ensure dist directory exists
    os.makedirs("dist", exist_ok=True)
    
    # Initial build
    rebuild_project()
    
    # Inject hot reload script into HTML files
    for html_file in Path("dist").glob("**/*.html"):
        inject_hot_reload_script(str(html_file))
    
    # Start Tailwind watcher
    tailwind_process = run_tailwind_watch()
    
    # Start WebSocket server for hot reload
    ws_server = WebSocketReloadServer(PORT + 1)
    ws_server.start()
    
    # Setup file watcher for hot reload
    observer = Observer()
    handler = HotReloadHandler(lambda: (
        rebuild_project() and ws_server.trigger_reload()
    ))
    
    # Watch src directory and main.py
    if os.path.exists("src"):
        observer.schedule(handler, "src", recursive=True)
    observer.schedule(handler, ".", recursive=False)
    observer.start()
    
    # Start HTTP server
    handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", PORT), handler)
    
    # Open browser
    webbrowser.open(f"http://localhost:{PORT}/dist")
    
    print(f"Development server running at http://localhost:{PORT}/dist")
    print("Hot reload enabled")
    print("Press Ctrl+C to stop the server")
    
    # Handle graceful shutdown
    def signal_handler(sig, frame):
        print("\n Shutting down server...")
        observer.stop()
        httpd.shutdown()
        if tailwind_process:
            tailwind_process.terminate()
        sys.exit(0)
    
    signal.signal(signal.SIGINT, signal_handler)
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        signal_handler(None, None)
