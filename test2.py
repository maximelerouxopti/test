# Ce programme calcule le périmètre d'un cercle dont
# le rayon a été demandé au clavier à l'utilisateur.

import math
import json
import requests


def meteo(la_ville):
    
    api = "London"
    return api


def ma_req(la_ville):
    my_key="959f090befe241b8c3993b96994a1cce"
    requete="http://api.openweathermap.org/data/2.5/weather?q=" + la_ville + "&APPID=" + my_key   
    return requete
    

    
def perimetre_cercle(un_rayon):
    """Calculer le périmètre d'un cercle à partir de son rayon.
	:param un_rayon: le rayon du cercle (positif)
	:return le périmètre d'un cercle de rayon un_rayon
    """
    diametre = 2 * un_rayon
    return math.pi * diametre


def main():
    """Le programme principal."""
    # demander le rayon à l'utilisateur
    ville = input("la ville : ")    # une chaîne de caractères
    la_ville = str(ville)                # convertie en un nombre réel
    mareq = la_ville +"test"
    print (mareq)

    # res = requests.get('http://api.openweathermap.org/data/2.5/weather?q=London&APPID=959f090befe241b8c3993b96994a1cce')
    # print(res.json())
    # calculer le périmètre
    # perimetre = perimetre_cercle(la_ville)
    print("la ville est ", la_ville)
    
     = ma_req(la_ville)    
    

    # afficher le périmètre à l'utilisateur
    print("la ville est ", la_ville , "l'api", api)

if __name__ == "__main__":
    main()
