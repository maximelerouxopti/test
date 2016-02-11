
#! /usr/bin/env python
# coding=utf-8

import random
import urllib2
# int annee;

print("hello");

annee =int(raw_input("Entrez un nombre: "))
print(annee);
i = 1;
while i < 2:
	x=random.randint(1,10);
	y=random.randint(1,10);
	print(x,"x",y);
	raw_input()
	z=x * y;
	i+=1;
	print(z);


class Rectangle:

	def __init__(self, long = 0.0, larg = 0.0, coul = "blanc"):
        	self.longueur = long
        	self.largeur = larg
        	self.couleur = coul

