import os
import sys
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from SimpleHTTPServer import SimpleHTTPRequestHandler
import json
import urllib

class customHTTPServer(SimpleHTTPRequestHandler):
  def do_OPTION(self):
    #https://developer.mozilla.org/En/Server-Side_Access_Control
    if self.headers['Origin'] == 'localhost.localdomain':
      self.send_response(200)
      self.send_header('Access-Control-Allow-Origin'  , 'localhost.localdomain')
      self.send_header('Access-Control-Allow-Methods' , 'POST, GET, OPTIONS')
      self.send_header('Access-Control-Allow-Headers' , 'X-PINGARUNER')
      self.send_header('Access-Control-Max-Age'       , '1728000')
      self.send_header('Content-Length'               , '0')
      self.send_header("Content-Type'                 ,  text/plain")
      self.end_headers()
    else:
      self.send_response(403)
      self.end_headers()

  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'application/x-www-form-urlencoded')
    #self.send_header('Accept', 'application/json')
    self.end_headers()
    self.wfile.write( urllib.quote(json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}]) ))
    #self.wfile.write( "hi!" )
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
    server = HTTPServer(('localhost', 8080),customHTTPServer)
    print 'server started at port 8080'
    server.serve_forever()
  except KeyboardInterrupt:
    server.socket.close()

if __name__=='__main__':
        main()
