#!/usr/bin/env python
# -*- coding: utf-8 -*
#http://python-3-patterns-idioms-test.readthedocs.io/en/latest/Factory.html
# A simple static factory method.
import sys
class Pizza:
  def __init__(self):
   pass
class PizzaSimple(Pizza):
    price=20,00
    def get_price(self):
        p=self.price
        print("Le prix de  SimplePizza égale à:"+ str(p) +"DA")
class PizzaThon(Pizza):
    price=30,00
    def get_price(self):
        p=self.price
        print("Le prix de TunaPizza égale à:"+ str(p) +"DA")
class PizzaMargarita(Pizza):
    price=40,00
    def get_price(self):
        p=self.price
        print("Le prix de MargaritaPizza égale à:"+ str(p) +"DA")
class PizzaFactory:
  def createPizza(self):
   pass
class PizzeriaLux (PizzaFactory):
   def createPizza(self):
     if   type == "PizzaThon":
            return PizzaThon()
     elif type == "PizzaMargarita":
            return PizzaMargarita()
     else:
        print ( "ce type n'existe pas" + type )

class PizzeriaHouma (PizzaFactory):
   def createPizza(self):
     if   type == "PizzaSimple":
            return PizzaSimple()
     elif type == "PizzaThon":
            return PizzaThon()
     else:
        print ( "ce type n'existe pas" + type )

if __name__ == '__main__':
    for type in ("PizzaThon","PizzaMargarita"):
         pizza=PizzeriaLux.createPizza(type)
         pizza.get_price()
    for type in ("PizzaSimple","PizzaThon"):
         pizza=PizzeriaHouma.createPizza(type)
         pizza.get_price()