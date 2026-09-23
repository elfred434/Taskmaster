# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 11:13:27 2026

@author: elfre
"""
from action import taches
def rechercher_taches():
    if not taches:
        print("Il n'y a aucune tâche à recherchez")
        return
    mot_cle = input("Entrez le mots").strip().lower()
    
    if not mot_cle:
        print("Aucun mot clé entré")
        return
    resultat = [t for t in taches if mot_cle in t["titre"].lower()]
    
    if not resultat:
        print(f"Y'a pas de tâches avec {mot_cle}")
        return
    print(f"{len(resultat)} résultat pour {mot_cle}")
    
    for num, fiche in enumerate(resultat, start=1):
        faite = "✔️" if fiche['faite'] else " "
        print(f"{num} . {fiche['titre']} {faite} {fiche['priorite']}")
        