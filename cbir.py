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

import math
import pygwt
import random

from __pyjamas__ import JS

class CBIR(Composite):
  def __init__(self):
    Composite.__init__(self)

    self.panel = DockPanel(HorizontalAlignment=HasAlignment.ALIGN_CENTER,
                           VerticalAlignment=HasAlignment.ALIGN_MIDDLE)
    self.panel.setWidth("100%")

    self.vp = VerticalPanel()

    self.grid = FlexTable(CellPadding=4, CellSpacing=4)
    self.grid.addTableListener(self)

    self.hp = HorizontalPanel()

    self.next   = Button("Next",    self, StyleName='button')
    self.finish = Button("Finish!", self, StyleName='button')
    self.clear  = Button("Clear",   self, StyleName='button')

    self.hp.add(self.clear)
    self.hp.add(self.finish)
    self.hp.add(self.next)
    self.hp.setWidth("70%")

    self.vp.add(Label("Content-Based Image Retrieval Using OPF", StyleName='label'))
    self.vp.add(self.grid)

    self.vp.setHorizontalAlignment(HasAlignment.ALIGN_RIGHT)
    self.vp.add(self.hp)

    cols = 4
    for i in range(100):
      im = Image('images/cbir/%d.jpg' % random.randint(0, 1000),  Size=("200px", "150px"), StyleName='image-cool')
      self.grid.setWidget(int(i/cols), i%cols, im)

    self.panel.add(self.vp, DockPanel.CENTER)

    self.initWidget(self.panel)

  def onCellClicked(self, sender, row, col):
    pass

  def onClick(self, sender):
    pass

class CBIRWeb:
  def onModuleLoad(self):
      self.cbir = CBIR()
      RootPanel().add(self.cbir)

if __name__ == '__main__':
    # for pyjd, set up a web server and load the HTML from there:
    # this convinces the browser engine that the AJAX will be loaded
    # from the same URI base as the URL, it's all a bit messy...
    pyjd.setup("public/index.html")
    app = CBIRWeb()
    app.onModuleLoad()
    pyjd.run()
