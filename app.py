from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(b"""
        <html>
        <body>
            <h1>Hello from GitHub Actions!</h1>
            <h2>Deployed from ECR to EC2 🚀</h2>
        </body>
        </html>
        """)

server = HTTPServer(("0.0.0.0", 3000), Handler)

print("Server running on port 3000")

server.serve_forever()
