# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 18:51:37 2016

@authors : Kinex & Papers
"""
from random import *
#class Attaque

class Equipement:
    def __init__(self, nom, modificateurs):
        self.nom=nom
        self.modificateurs={
            "CONSTITUTION" : modificateurs[0], #Constitution
            "FORCE" : modificateurs[1], #Force
            "AGILITE" : modificateurs[2] #Agilité
        }
        #self.owner..

    def getMod(self, TYPE):
        if TYPE not in ["CONSTITUTION", "FORCE", "AGILITE"]:
            raise ValueError("Caractéristique incorrecte")
        else:
            return self.modificateurs[TYPE]

class Caracteristique:
    def __init__(self, TYPE, baseValue):
        if TYPE not in ["CONSTITUTION", "FORCE", "AGILITE"]:
            raise ValueError("Caractéristique incorrecte")
        else:
            self.TYPE=TYPE
        self.baseValue=baseValue
        self.modifiers=dict()
        self.value=self.updateValue()

    def attachEquipements(self, *equipement):
        for i in equipement:
            self.modifiers[i.name]=i.getMod(self.TYPE)
        self.updateValue()

    def updateValue(self):
        value=self.baseValue
        for i in self.modifiers.values():
            ##extract value
            value += i
        return value

    def getValue(self):
        return self.value


class Personnage:
    def __init__(self, nom, vie=100, mana=100):
        ##Base de la base
        self.nom=nom
<<<<<<< Updated upstream
        self.vie_max=Caracteristique(vie)
        self.vie_courante=self.vie_max.getValue()
        self.mana=mana

        ##Caractéristiques influencables par l'équipmt
        self.force=Caracteristique(100)
        self.agilite=Caracteristique(30)
        self.constitution=Caracteristique(30)
=======
        self.vie=vie
        self.force=100
        self.defense
        self.constitution=100
>>>>>>> Stashed changes
        # vie : max et courante
        # attaque  --> Air/feu/eau/terre
        # defense  --> Idem
        # mana
        # résistance
        
    def attaquer(self, autrePerso):
<<<<<<< Updated upstream
        degats=self.baseAttaque+self.attaqueModifier+self.force/10
=======
        degats=(force/2)+(randint(-100,100)/100)*(force/2) # les degats donnes ont comme valeur max force/2+force/2 = force et comme valeur min force/2=force/2=0
        ##mod des degats
>>>>>>> Stashed changes
        autrePerso.defendre(degats)
        
    def defendre(self, degatsRecus):
        ##mod des degats recus
        degatsFinaux=degatsRecus-(randint(0,100)/100*defense) # on soustrait aux degats recus au maximum "defense".
        self.vie-=degatsFinaux
        
    def getVie(self):
        print(self.nom+" a encore "+str(self.vie)+" pdv")       
        
    def __repr__(self):
        return "Personnage : nommé "+self.nom+" avec "+str(self.vie)+" pdv"
        
Max=Personnage("Max")
DarkSieg=Personnage("DarkSieg")

Max.attaquer(Personnage)