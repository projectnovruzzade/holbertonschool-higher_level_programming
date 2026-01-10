#!/usr/bin/python3
""" this is external enviroment"""

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse
import json


class SimpleAPIHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("PATH:", self.path)
        parsed_path = urlparse(self.path).path
        print("PATH:", parsed_path)

        if parsed_path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif parsed_path == "/data":
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }

            response = json.dumps(data).encode("utf-8")

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(response)

        elif parsed_path == "/info":
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }

            response = json.dumps(info).encode("utf-8")

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(response)

        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


server = HTTPServer(("localhost", 8000), SimpleAPIHandler)
print("Server running at http://localhost:8000")
server.serve_forever()
