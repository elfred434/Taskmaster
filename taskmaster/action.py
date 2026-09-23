# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 10:27:01 2026

@author: elfre
"""


from stockage import taches, demander_entier, sauvegader
  


        
    
    
    
    
def voir_fiches():
    if not taches:
        print("Aucune tâches enregistrées")
    
    print(f"Il y'a {len(taches)} taches")
    for num, fiche in enumerate(taches, start=1):
        faite = "✔️" if fiche['faite'] else " "
        print(f"{num} . {fiche['titre']} {faite}")
    return

def marquer_faite():
    if not taches:
        print("Il n'y a aucune tâches enregistrés")
    voir_fiches()
    
    try:
        num = demander_entier("Entrez le numéro de la tâches")
        taches[num - 1] ['faite']= True
        sauvegader(taches)
        print("C'est coché")
    except IndexError:
         print("Numéro invalide")
    except ValueError:
         print("Entrez un chiffre")
    return  

def supprimer_taches():
    if not taches:
        print("Never task save")
    voir_fiches()
    
    try:
        num = demander_entier("Entez the num of task  deleted")
        del taches[num -1]
        sauvegader(taches)
        print("C'est effacé")
    except IndexError:
        print("numéro invalide")
    except ValueError:
        print("Entez a chiffre")
    return   