import pyjd # this is dummy in pyjs.
from pyjamas import DOM

from pyjamas.ui.RootPanel import RootPanel, RootPanelCls, manageRootPanel
from pyjamas.ui.HTML import HTML
from pyjamas.ui.Label import Label
from pyjamas.ui.Hyperlink import Hyperlink
from pyjamas.ui.HTML import HTML
from pyjamas.ui.Image import Image
from pyjamas.ui.Button import Button
from pyjamas.ui.DockPanel import DockPanel
from pyjamas.ui.VerticalPanel import VerticalPanel
from pyjamas.ui.HorizontalPanel import HorizontalPanel
from pyjamas.ui import HasAlignment
from pyjamas.ui.DockPanel import DockPanel
from pyjamas.ui.Composite import Composite
from pyjamas.ui.FlexTable import FlexTable

from pyjamas.HTTPRequest import HTTPRequest
from pyjamas.JSONService import JSONProxy
import urllib

try:
    # included in python 2.6...
    from json import dumps, loads
except ImportError:
    try:
        # recommended library (python 2.5)
        from simplejson import dumps, loads
    except ImportError:
        # who's the pyjs daddy?
        from pyjamas.JSONParser import JSONParser
        parser = JSONParser()
        dumps = getattr(parser, 'encode')
        loads = getattr(parser, 'decodeAsObject')
        JSONDecodeException = None



import math
import pygwt
import random

from __pyjamas__ import JS

class CBIR(Composite):
  def __init__(self):
    Composite.__init__(self)

    panel = DockPanel(HorizontalAlignment=HasAlignment.ALIGN_CENTER,
                      VerticalAlignment=HasAlignment.ALIGN_MIDDLE)
    panel.setWidth("100%")

    vp = VerticalPanel()

    grid = FlexTable(CellPadding=4, CellSpacing=4)

    hp = HorizontalPanel()

    self.next   = Button("Next",    self, StyleName='button')
    self.finish = Button("Finish!", self, StyleName='button')
    self.clear  = Button("Clear",   self, StyleName='button')

    hp.add(self.clear)
    hp.add(self.finish)
    hp.add(self.next)
    hp.setWidth("70%")

    vp.add(Label("Content-Based Image Retrieval Using OPF", StyleName='label'))
    vp.add(grid)

    vp.setHorizontalAlignment(HasAlignment.ALIGN_RIGHT)
    vp.add(hp)

    cols = 4
    for i in range(100):
      im = Image('images/cbir/%d.jpg' % random.randint(0, 1000),  Size=("200px", "150px"), StyleName='image-cool')
      grid.setWidget(int(i/cols), i%cols, im)

    panel.add(vp, DockPanel.CENTER)

    self.initWidget(panel)

    self.status = Label()
    vp.add(self.status)

    self.remote_py = TestService()

  def onModuleLoad(self):
    self.TEXT_WAITING = "Waiting for response..."
    self.TEXT_ERROR = "Server Error"

  def onClick(self, sender):
    self.status.setText(self.TEXT_WAITING)
    id = self.remote_py.add(10, 20, self)

  def onRemoteResponse(self, response, request_info):
    self.status.setText(response)

    #msg = dumps( {'spam':1, 'eggs':2} )
    #print msg
    #params = urllib.quote(msg, safe="")
    #header = {'Content-Type': 'application/x-www-form-urlencoded', 'Accept':'application/json'}
    #HTTPRequest().asyncPost(url="http://localhost:8000", postData=params, handler=HandlePOST(self), headers=header)
    #HTTPRequest().asyncGet (url="http://localhost:8000/index.html", content_type='application/x-www-form-urlencoded',  handler=HandleGET(self), headers=header)

  def onRemoteError(self, code, errobj, request_info):
      # onRemoteError gets the HTTP error code or 0 and
      # errobj is an jsonrpc 2.0 error dict:
      #     {
      #       'code': jsonrpc-error-code (integer) ,
      #       'message': jsonrpc-error-message (string) ,
      #       'data' : extra-error-data
      #     }
      message = errobj['message']
      if code != 0:
          self.status.setText("HTTP error %d: %s" %
                              (code, message))
      else:
          code = errobj['code']
          self.status.setText("JSONRPC Error %s: %s" %
                              (code, message))

#class HandleGET:
#  def __init__ (self, app):
#    self.app = app
#
#  def onCompletion(self, response):
#    self.app.status.setText(response)
#    print "GET completed!", response
#
#class HandlePOST:
#  def __init__ (self, app):
#    self.app = app
#
#  def onCompletion(self, response):
#    self.app.status.setText(response)
#    print "POST completed!", response

class TestService(JSONProxy):
  def __init__(self):
    JSONProxy.__init__(self, "http://localhost:8080", ["add", "ping"])

class CBIRWeb:
  def onModuleLoad(self):
    self.cbir = CBIR()
    self.cbir.onModuleLoad()
    RootPanel().add(self.cbir)

if __name__ == '__main__':
    # for pyjd, set up a web server and load the HTML from there:
    # this convinces the browser engine that the AJAX will be loaded
    # from the same URI base as the URL, it's all a bit messy...
    pyjd.setup("http://localhost:8080/index.html")
    app = CBIRWeb()
    app.onModuleLoad()
    pyjd.run()
