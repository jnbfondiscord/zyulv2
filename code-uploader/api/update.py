import os
from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers['Content-Length'])
        body = self.rfile.read(length)
        data = json.loads(body)
        code = data.get('code', '')

        with open('/tmp/code.txt', 'w') as f:
            f.write(code)

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Updated')
