from http.server import *
from http_statuses import *


class CurrentStartpoint(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTP_OK)

        self.send_header('content-type', 'text/html')
        self.end_headers()

        self.wfile.write('<h1>welcome!</h1>'.encode())


port = HTTPServer(('', 8080), CurrentStartpoint)

port.serve_forever()