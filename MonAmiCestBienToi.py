# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 18:51:37 2016

@author: Kinex
"""

#class Attaque

class Caracteristique:
    def __init__(self, ):
        self

class Personnage:
    def __init__(self, nom, vie=100):
        self.nom=nom
        self.vie=vie
        self.attaqueModifier=0
        self.baseAttaque
        self.force
        # vie : max et courante
        # attaque  --> Air/feu/eau/terre
        # defense  --> Idem
        # mana
        # résistance
        
    def attaquer(self, autrePerso):
        degats=self.baseAttaque+self.attaqueModifier+self.force/10
        autrePerso.defendre(degats)
        
    def defendre(self, degatsRecus):
        ##mod des degats recus
        degatsFinaux=degatsRecus
        self.vie-=degatsFinaux
        
    def getVie(self):
        print(self.nom+" a encore "+str(self.vie)+" pdv")       
        
    def __repr__(self):
        return "Personnage : nommé "+self.nom+" avec "+str(self.vie)+" pdv"
        
Max=Personnage("Max")
DarkSieg=Personnage("DarkSieg")

Max.attaquer(Personnage)