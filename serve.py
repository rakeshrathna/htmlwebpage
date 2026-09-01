import http.server
import socketserver
import os

PORT = 3000

class NoCacheHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

os.chdir(r'c:\Users\admin\Downloads\HTML GAME')

with socketserver.TCPServer(('', PORT), NoCacheHTTPRequestHandler) as httpd:
    print(f'Serving at http://localhost:{PORT} with NO-CACHE headers')
    httpd.serve_forever()
