import json
from http.server import BaseHTTPRequestHandler
import urllib.parse
import os

# Path to the JSON file
json_file_path = os.path.join(os.getcwd(), "q-vercel-python.json")

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse query parameters (extract "name" values)
        query_components = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
        names = query_components.get('name', [])

        # Load student data from the JSON file
        try:
            with open(json_file_path, "r") as f:
                student_data = json.load(f)
        except FileNotFoundError:
            student_data = []

        # Prepare the response
        marks = []
        for name in names:
            # Search for the student's marks by their name
            found = False
            for student in student_data:
                if student['name'] == name:
                    marks.append(student['marks'])
                    found = True
                    break
            if not found:
                marks.append("Not found")

        # Send response
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({"marks": marks}).encode('utf-8'))
        return
