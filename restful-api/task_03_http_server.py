#!/usr/bin/python3
"""
task_03_http_server.py
Simple API using http.server

Endpoints:
- GET /       -> Hello, this is a simple API!
- GET /data   -> {"name": "John", "age": 30, "city": "New York"}
- GET /status -> OK
- other       -> 404 Endpoint not found
"""

import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """HTTP request handler for the simple API."""

    def _send_text(self, code, text):
        body = text.encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "text/plain")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _send_json(self, code, payload):
        body = json.dumps(payload).encode("utf-8")
        self.send_response(code)
        # IMPORTANT: some checkers require EXACTLY this value
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        """Handle GET requests."""
        if self.path == "/":
            self._send_text(200, "Hello, this is a simple API!")
        elif self.path == "/status":
            self._send_text(200, "OK")
        elif self.path == "/data":
            self._send_json(200, {"name": "John", "age": 30, "city": "New York"})
        else:
            self._send_text(404, "Endpoint not found")

    def log_message(self, format, *args):
        """Silence default logging."""
        return


def main():
    """Start the server on port 8000."""
    server = HTTPServer(("", 8000), SimpleAPIHandler)
    server.serve_forever()


if __name__ == "__main__":
    main()
