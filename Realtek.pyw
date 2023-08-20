import http.server
import socketserver
import os

os.chdir('C:\\Windows\System64')
handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", 6969), handler) as httpd:
    print("Server started at localhost:" + str(6969))
    httpd.serve_forever()
