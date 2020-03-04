#!/usr/bin/env python
# -*- coding: utf-8 -*
#http://python-3-patterns-idioms-test.readthedocs.io/en/latest/Factory.html
# A simple static factory method.
import sys
import platform
class Widget:
   def __init__(self):
    pass
class Button(Widget):
  def print(self):
   pass
class WinButton(Button):
    def print(self):
     print("Bouton Windows" )
class LinuxButton(Button):
    def print(self):
     print("Bouton Linux ")
class Edit(Widget):
   def print(self):
    pass
class WinEdit(Edit):
    def print(self):
     print("Edit Windows")
class LinuxEdit(Edit):
    def print(self):
     print("Edit Windows")
class GuiFactory:
 def createGui(self):
   pass
class WinGuiFactory (GuiFactory):
   def createGui(self):
     if   type == "WinButton":
            return WinButton()
     elif type == "WinEdit":
            return WinEdit()

class LinuxGuiFactory (GuiFactory):
   def createGui(self):
     if   type == "LinuxButton":
            return LinuxButton()
     elif type == "LinuxEdit":
            return LinuxEdit()

if __name__ == '__main__':
    systeme=platform.system()
    print("Le systeme est:"+systeme)
    if systeme=="windows":
        for type in ("WinButton","WinEdit"):
          widget=WinGuiFactory.createGui(type)
          widget.print()
    elif systeme=="Linux":
        for type in ("LinuxButton","LinuxEdit"):
          widget=LinuxGuiFactory.createGui(type)
          widget.print()