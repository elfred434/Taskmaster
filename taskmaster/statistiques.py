# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 10:50:11 2026

@author: elfre
"""
from stockage import taches

def afficher_statistiques():
    if not taches:
        print("Il n'y aucune taches enregistrés")
        return
    total = len(taches)
    faites = len([t for t in taches if t["faite"]])
    restant = len([t for t in taches if not t['faite']])
    haute = len([t for t in taches if t["priorite"] == "haute"])
    normale = len([t for t in taches if t["priorite"] == "normale"])
    
    print("===Statistiques===")
    print(f"Total : {total}")
    print(f"Faites: {faites}")
    print(f"Restante: {restant}")
    print(f"Haute: {haute}")
    print(f"Normale: {normale}")
    