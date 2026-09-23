# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 10:27:01 2026

@author: elfre
"""


from stockage import taches, demander_entier, sauvegarder
  


        
    
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
    sauvegarder(taches)
    print(f"✔️ Fiche de  {titre} enregistrée")    
    
    
def voir_fiches():
    if not taches:
        print("Aucune tâches enregistrées")
    #tier
    taches_tries = sorted(taches, key=lambda t:0 if t['priorite']== "haute" else 1)
    print(f"Il y'a {len(taches)} taches")
    for num, fiche in enumerate(taches_tries, start=1):
        faite = "✔️" if fiche['faite'] else " "
        print(f"{num} . {fiche['titre']} {faite}  {fiche['priorite']}")
    return taches_tries

def marquer_faite():
    if not taches:
        print("Il n'y a aucune tâches enregistrés")
    taches_tries = voir_fiches()
    
    try:
        num = demander_entier("Entrez le numéro de la tâches")
        #taches[num - 1] ['faite']= True
        fiche = taches_tries[num - 1]
        fiche['faite'] = True
        sauvegarder(taches)
        print("C'est coché")
    except IndexError:
         print("Numéro invalide")
    except ValueError:
         print("Entrez un chiffre")
    return  

def supprimer_taches():
    if not taches:
        print("Never task save")
    taches_tries = voir_fiches()
    
    try:
        num = demander_entier("Entez the num of task  deleted")
        fiches = taches_tries[num -1]
        index = taches.index(fiches)
        del taches[index]
        sauvegarder(taches)
        print("C'est effacé")
    except IndexError:
        print("numéro invalide")
    except ValueError:
        print("Entez a chiffre")
    return   