#!/usr/bin/python3
"""
Task 03: Develop a simple API using Python's http.server module.

Endpoints:
- GET /        -> "Hello, this is a simple API!"
- GET /data    -> JSON: {"name": "John", "age": 30, "city": "New York"}
- GET /status  -> "OK"
- Any other    -> 404 "Endpoint not found"
"""

import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """Request handler for a tiny REST-like API."""

    def _send_text(self, status_code, message):
        """Send a plain text response."""
        body = message.encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _send_json(self, status_code, payload):
        """Send a JSON response."""
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        """Handle GET requests for supported endpoints."""
        if self.path == "/":
            self._send_text(200, "Hello, this is a simple API!")
        elif self.path == "/status":
            self._send_text(200, "OK")
        elif self.path == "/data":
            self._send_json(200, {"name": "John", "age": 30, "city": "New York"})
        else:
            self._send_text(404, "Endpoint not found")

    def log_message(self, format, *args):
        """Optional: silence default logging (keeps output clean)."""
        return


def run(server_class=HTTPServer, handler_class=SimpleAPIHandler, port=8000):
    """Start the HTTP server."""
    server_address = ("", port)  # bind all interfaces
    httpd = server_class(server_address, handler_class)
    print(f"Serving on http://localhost:{port}")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
