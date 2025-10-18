import http.server
import socketserver
import os
import threading
import subprocess

PORT = 8000

def run_tailwind_watch():
    """Start Tailwind CSS process if config exists"""
    if os.path.exists("tailwind.config.js"):
        try:
            subprocess.run(
                ["npx", "tailwindcss", "-i", "./input.css", "-o", "./tailwind.css", "--watch"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            print("Tailwind CSS is watching for changes...")
        except FileNotFoundError:
            print("Tailwind CSS is not installed. Please install it to use this feature.")
    else:
        print("No Tailwind CSS configuration found. Skipping Tailwind watch.")

def run_dev_server():
    """Run the local dev server"""
    handler = http.server.SimpleHTTPRequestHandler
    os.makedirs("dist", exist_ok=True)
    os.chdir(".")

    run_tailwind_watch()

    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print(f"Serving at http://localhost:{PORT}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("Shutting down server...")
            httpd.shutdown()
