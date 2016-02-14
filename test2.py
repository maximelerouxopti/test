#! /usr/bin/env Python
# -*- coding: utf-8 -*-


import random
import urllib2
import os
# int annee;

print("hello");

annee =int(raw_input("Entrez un nombre: "))
print(annee);
i = 0;
while i < 2:
	x=random.randint(1,10);
	y=random.randint(1,10);
	print(x,"x",y);
	#raw_input()
	z=x * y;
	i+=1;
	print(z);


class Rectangle:
    "ceci est la classe Rectangle"
    def __init__(self, long = 0.0, larg = 0.0, coul = "blanc"):
        self.longueur = long
        self.largeur = larg
        self.couleur = coul
    # définition de la méthode qui calcule la surface
    def calculSurface(self):
        print "surface = %.2f m2" %(self.longueur * self.largeur)
    # définition de la méthode qui transforme un rectangle en carré
    def changeCarre(self, cote):
        self.longueur = cote
        self.largeur = cote