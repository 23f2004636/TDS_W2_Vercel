import json
from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Open and load the JSON file containing the data
        with open("q-vercel-python.json", 'r') as file:
            data = json.load(file)

        # Send a 200 response and content type as JSON
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        # Write the JSON data to the response
        self.wfile.write(json.dumps(data).encode('utf-8'))
        return
