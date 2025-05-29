import http.server
import socketserver

PORT = 8000
DIRECTORY = "."

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

print(f"🚀 Shane's Repair Shop is live at http://localhost:{PORT} 🚀")
print("Press Ctrl+C to stop the server...")

try:
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        httpd.serve_forever()
except KeyboardInterrupt:
    print("\n🛠️ Server stopped. Thanks for fixing stuff, Shane! 😎")