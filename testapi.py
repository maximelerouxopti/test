#!/usr/bin/python
# -*- coding: utf-8 -*-

import py
import urllib2
import os
import os.path
import json
import sys

#def hello(arg1, arg2):
#    print arg1, arg2

#je fais des tests
#pouet
#yolo pc boulot
# http://api.openweathermap.org/data/2.5/forecast/city?id=524901&APPID=959f090befe241b8c3993b96994a1cce
# curl -0 -L "https://disqus.com/api/3.0/trends/listThreads.json?api_key=API_PUBLIC_KEY_HERE&callback=foo"
#from twitter import *

#t = Twitter(
#    auth=OAuth(token, token_secret, consumer_key, consumer_secret))

#def requete(ville):
#    villefc= 
#    return req


def main():
    """Le programme principal."""
   # ville = input("entrer la ville:")
   # la_ville = str(ville)
   # req = requete(la_ville)
    try:
       page_json = urllib2.urlopen('http://api.openweathermap.org/data/2.5/weather?q=Paris&APPID=959f090befe241b8c3993b96994a1cce')
    # Je lis la page
       json_string = page_json.read()
    # Je mets cette page dans un parseur
       parsed_json = json.loads(json_string)
    # Et je peux fermer ma page meteo, je n'en ai plus besoin
       page_json.close()
       print("coucou")
    except:
        print("ca marche pas")
        sys.exit(2)    
    
    city = parsed_json['name'] # la ville
   # weather = parsed_json['weather']['main'] # l'heure dernière observation
    current_temp = parsed_json['main']['temp'] # la température en °C
    current_temp = current_temp -273;
    print (city)
    print (current_temp)
    #    ville = input("entrer la ville : ")    # une chaîne de caractères
    #    mareq=requete
    #le_rayon = float(saisie)                # convertie en un nombre réel
    # calculer le périmètre
    #perimetre = perimetre_cercle(le_rayon)
    # afficher le périmètre à l'utilisateur
    #print("Le périmètre d'un cercle de rayon", le_rayon, "est", perimetre)

if __name__ == "__main__":
    main()


def requete (ville):
    req= 'http://api.openweathermap.org/data/2.5/weather?q=Paris&APPID=959f090befe241b8c3993b96994a1cce'
    print req
    return req

