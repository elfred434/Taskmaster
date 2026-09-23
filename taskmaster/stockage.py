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

def ajouter_taches():
    titre= input("Entrez le titre de la taches").strip().title()
    faite = False
    prorite = input("Choisissez entre haute, normale")
    
    fiche = {
         "titre":titre,
        "faite": faite,
        "priorite": prorite
        }
    taches.append(fiche)
    sauvegader(taches)
    print(f"✔️ Fiche de  {titre} enregistrée")
    
def sauvegader(tache, fichier="Taches.json"):
    try:
        with open(fichier, "w") as f:
            json.dump(taches, f)
            print(f"Il y'a {len(taches)} tâches sauvegardés dans {fichier}")
    except Exception as e:
        print(f"Erreur de sauvegarde {e}")
        
        

    

