#!/usr/bin/env python
# -*- coding: utf-8 -*
#http://python-3-patterns-idioms-test.readthedocs.io/en/latest/Factory.html
# A simple static factory method.
import sys
class Shape():
 def __init__(self):
   pass
class Circle(Shape):
   def draw(self) :
        print("Circle.draw")
   def erase(self):
    print("Circle.erase")
class Circle2D(Circle):
    def draw(self) :
        print("Circle.draw2D")
    def erase(self):
        print("Circle.erase2D")
class Circle3D(Circle):
    def draw(self) :
        print("Circle.draw3D")
    def erase(self):
        print("Circle.erase3D")
class Square(Shape):
    def draw(self) :
        print("Square.draw")
    def erase(self):
        print("Square.erase")
class Square2D(Square):
    def draw(self) :
        print("Square.draw2D")
    def erase(self):
        print("Square.erase2D")
class Square3D(Square):
    def draw(self) :
        print("Square.draw3D")
    def erase(self):
        print("Square.erase3D")

class ShapeFactory:
    @staticmethod
    def createShape(type):
        pass
class ShapeFactory2D(ShapeFactory):
    @staticmethod
    def createShape(type):
        if   type == "Circle":
            return Circle2D()
        elif type == "Square":
            return Square2D()
        else:  return None
class ShapeFactory3D(ShapeFactory):
    @staticmethod
    def createShape(type):
        if   type == "Circle":
            return Circle3D()
        elif type == "Square":
            return Square3D()
        else:  return None
if __name__ == '__main__':

 for type in ("Circle", "Square" ,"Circle", "Square"):
    #shape = ShapeFactory2D.createShape(type)
    shape = ShapeFactory3D.createShape(type)
    shape.draw()
    shape.erase()