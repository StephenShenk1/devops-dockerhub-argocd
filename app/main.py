from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello from DevOps pipeline with Docker Hub and ArgoCD!')

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 80), Handler)
    print("Serving on port 80...")
    server.serve_forever()
