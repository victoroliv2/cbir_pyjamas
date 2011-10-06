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

class NextHandle:
  def __init__ (self, app):
    self.app = app

  def onCompletion(self, response):
    self.app.status.setText(response)
    print "GET completed!", response

  def onClick(self, sender):
    self.app.status.setText(self.app.TEXT_WAITING)

    HTTPRequest().asyncGet (url = "http://0.0.0.0:8080/",
                            handler = self)
                            
class FinishHandle:
  def __init__ (self, app):
    self.app = app

  def onCompletion(self, response):
    self.app.status.setText(response)
    print "POST completed!", response

  def onClick(self, sender):
    self.app.status.setText(self.app.TEXT_WAITING)
    msg = dumps( {'spam':1, 'eggs':2} )

    HTTPRequest().asyncPost(url = "http://0.0.0.0:8080/",
                            postData = msg,
                            handler = self)

class ClearHandle:
  def onClick(self, sender):
    pass

class CBIR(Composite):
  def __init__(self):
    Composite.__init__(self)

    panel = DockPanel(HorizontalAlignment=HasAlignment.ALIGN_CENTER,
                      VerticalAlignment=HasAlignment.ALIGN_MIDDLE)
    panel.setWidth("100%")

    vp = VerticalPanel()

    grid = FlexTable(CellPadding=4, CellSpacing=4)

    hp = HorizontalPanel()

    handle_n = NextHandle(self)
    handle_f = FinishHandle(self)
    handle_c = ClearHandle(self)

    self.next   = Button("Next",    handle_n, StyleName='button')
    self.finish = Button("Finish!", handle_f, StyleName='button')
    self.clear  = Button("Clear",   handle_c, StyleName='button')

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

  def onModuleLoad(self):
    self.TEXT_WAITING = "Waiting for response..."
    self.TEXT_ERROR = "Server Error"
                            
    return True

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
