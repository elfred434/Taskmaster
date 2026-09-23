# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 10:25:46 2026

@author: elfre
"""
#import stockage
from action import voir_fiches, marquer_faite, supprimer_taches, ajouter_taches
from statistiques import afficher_statistiques
from rechercher import rechercher_taches
app_name= "Taskmaster"
auteur = "Elfred Dangbenon"
version = 0.1

print("======================")

print(f"   {app_name} v{version}") 
print("  ","par",auteur )
print("======================")



def afficher_menu():
    print("Entrez 1 pour ajoutez une tâche ")
    print("Entrez 2 pour voir vos tâches ")
    print("Entrez 3 pour marquez comme lu ")
    print("Entrez 4 pour supprimé")
    print("Entrez 5 pour voir les statistiques")
    print("Entrez 6 pour recherchez")
    print("Entrez 7 pour quitter")
    choix = input("Ton choix ")
    return choix

def main():
    while True:
        choix = afficher_menu()
        if choix == "1":
            ajouter_taches()
        elif choix == "2":
             voir_fiches()
        elif choix == "3":
            marquer_faite()
        elif choix == "4":
            supprimer_taches()
        elif choix == "5":
            afficher_statistiques()
        elif choix == "6":
            rechercher_taches()
        elif choix == "7":
            print("A bientôt !")
            break
        else:
             print("Choix invalides")

if __name__ == "__main__":
    main()