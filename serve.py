import http.server
import socketserver
import webbrowser

PORT = 8000
URL = f"http://localhost:{PORT}"

print("\n" + "=" * 55)
print(" 🎂  Gundumani's Birthday Website Local Server")
print("=" * 55)
print(f"\n 👉 CLICKABLE LINK:  \033[4;36m{URL}\033[0m\n")
print(" Press Ctrl+C in terminal to stop the server.\n" + "=" * 55 + "\n")

# Automatically open in browser
try:
    webbrowser.open(URL)
except Exception:
    pass

# Start HTTP Server
Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
