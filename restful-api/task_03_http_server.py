#!/usr/bin/python3
""" this is external enviroment"""

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse
import json


class SimpleAPIHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path).path
        print("PATH RECEIVED:", parsed_path)

        if parsed_path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            response = json.dumps(data).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(response)
            return

        if parsed_path == "/info":
            info = {"version": "1.0", "description": "A simple API built with http.server"}
            response = json.dumps(info).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(response)
            return

        if parsed_path == "/status":
            # This is the new endpoint the test expects
            status = {"status": "OK"}
            response = json.dumps(status).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(response)
            return

        if parsed_path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
            return

        if parsed_path == "/favicon.ico":
            self.send_response(204)
            self.end_headers()
            return

    # Everything else
    self.send_response(404)
    self.send_header("Content-Type", "text/plain")
    self.end_headers()
    self.wfile.write(b"Endpoint not found")


server = HTTPServer(("localhost", 8000), SimpleAPIHandler)
print("Server running at http://localhost:8000")
server.serve_forever()
