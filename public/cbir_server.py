import os
import sys
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import json
import urllib

class customHTTPServer(BaseHTTPRequestHandler):
        def do_GET(self):
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write( json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}]) )
                return

        def do_POST(self):
                if self.headers['Accept'] != 'application/json':
                  self.send_response(406) # Not acceptable
                  return

                length = int( self.headers['Content-Length'] )
                data = json.loads( urllib.unquote( self.rfile.read(length) ))
                print data
                self.send_response(201)
                self.end_headers()
                self.wfile.write('Post!')

def main():
        try:
                server = HTTPServer(('localhost', 8000),customHTTPServer)
                print 'server started at port 8000'
                server.serve_forever()
        except KeyboardInterrupt:
                server.socket.close()

if __name__=='__main__':
        main()
