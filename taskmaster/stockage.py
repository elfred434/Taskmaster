# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 10:26:49 2026

@author: elfre
"""
import json

FICHIER = "Taches.json"

def charger(fichier=FICHIER):
    try:
        with open(fichier, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print(f"{fichier}fichier corrompu ou vide")
        return []
        
taches = charger()

def demander_entier(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Please enter a integrer nomber")


    
def sauvegarder(tache, fichier="Taches.json"):
    try:
        with open(fichier, "w") as f:
            json.dump(tache, f)
            print(f"Il y'a {len(taches)} tâches sauvegardés dans {fichier}")
    except Exception as e:
        print(f"Erreur de sauvegarde {e}")
        
        

    

