#!/usr/bin/env python
# -*- coding: utf-8 -*
#http://python-3-patterns-idioms-test.readthedocs.io/en/latest/Factory.html
# A simple static factory method.
import sys
class Compte:
  def stock(self):
     print("Fonction Stocke ")
  def achat(self):
     print("Fonction Achat ")
  def commande(self):
     print("Fonction Commande ")

class Vendeur(Compte):
   def stock(self):
     print ( "Fonction Stock Vnedeur " )
   def achat(self):
     print ( "Fonction Achat Vnedeur " )
   def commande(self):
     print ( "Fonction Commande Vnedeur ")
   def conuslter_recette(self):
    print ( "Vous n'avez pas accès à cette Fonction  ")


class Visiteur(Compte):
   def stock(self):
     print ( "Fonction Consulter Le Stock " )
   def achat(self):
     print ( "Fonction Achat Visiteur " )
   def commande(self):
     print ( "Fonction Commande Visiteur ")
   def conuslter_recette(self):
    print ( "Vous n'avez pas accès à cette Fonction  ")

class Gestionnaire(Compte):
   def stock(self):
     print ( "Fonction  Gérer Le Stock" )
   def achat(self):
     print ( "Fonction Achat Gestionnaire " )
   def commande(self):
     print ( "Fonction  Commande Gestionnaire ")
   def conuslter_recette(self):
    print ( " Fonction Conuslter la recette  ")
class CompteFactory:
   def createCompte(self):
       pass
class ConcreteCompteFactory(CompteFactory):
    def createCompte(self):
      if (type == "Vendeur"):
         return Vendeur()
      elif (type == "Gestionnaire"):
         return Gestionnaire()
      elif (type == "Visiteur"):
         return Visiteur()
if __name__ == '__main__':
   for type in ("Vendeur", "Gestionnaire", "Visiteur"):
      co= ConcreteCompteFactory.createCompte(type)
      co.stock()
      co.achat()
      co.commande()
      co.conuslter_recette()

