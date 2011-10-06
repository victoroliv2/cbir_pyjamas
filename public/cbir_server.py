import os
import sys
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from SimpleHTTPServer import SimpleHTTPRequestHandler
import json
import urllib

class customHTTPServer(SimpleHTTPRequestHandler):
        def do_GET(self):
                self.send_response(200)
                self.send_header('Content-type', 'application/x-www-form-urlencoded')
                self.send_header('Accept', 'application/json')
                self.end_headers()
                #self.wfile.write( urllib.quote(json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}]) ))
                self.wfile.write( "hi!" )
                return

        def do_POST(self):
                if self.headers['Accept'] != 'application/json':
                  self.send_response(406) # Not acceptable
                  return

                length = int( self.headers['Content-Length'] )
                data = json.loads( urllib.unquote( self.rfile.read(length) ))
                print data
                self.send_response(200)
                self.send_header('Content-type', 'application/x-www-form-urlencoded')
                self.send_header('Accept', 'application/json')
                self.end_headers()
                self.wfile.write( urllib.quote(json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])  ))
                return

def main():
        try:
                server = HTTPServer(('localhost', 8000),customHTTPServer)
                print 'server started at port 8000'
                server.serve_forever()
        except KeyboardInterrupt:
                server.socket.close()

if __name__=='__main__':
        main()
