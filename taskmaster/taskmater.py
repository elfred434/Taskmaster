# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 13:52:31 2026

@author: elfre
"""
app_name= "Taskmaster"
auteur = "Elfred Dangbenon"
version = 0.1

print("======================")
#print("  ",app_name,"v"+str(version))
print(f"   {app_name} v{version}") 
print("  ","par",auteur )
print("======================")
"""
#Demande de taches de l'utilisateur
taches = []
tache= input("Entrez votre tâches ")
taches_net = tache.strip().title()
taches.append(taches_net)

print("✔️ Tâche enregistrée :", taches_net)
print("longueur :",len(taches_net))
print(f"Tu as maintenant {len(taches)} tâches(s)")

for t in taches:
    print("-", t)"""
    
#Demande de tâche à l'utilisateur avec boucle
taches = []

"""
    tache= input("Entrez votre tâches ")  
    if tache.lower().strip() == "stop":
       
        break
    taches_net = tache.strip().title()
    taches.append(taches_net)
    print("✔️ Tâche enregistrée :", taches_net)
print("longueur :",len(taches_net))
print(f"Tu as maintenant {len(taches)} tâches(s)")
for num, t in enumerate(taches, start=1):
    print(f"{num}. {t}")"""
    
    
def ajouter_taches(taches):
    while True:
        tache = input("Entrez votre tâches ")
        if tache.lower().strip() == "stop":
            break
        taches_net = tache.strip().title()
        taches.append(taches_net)
        print("✔️ Tâche enregistrée :", taches_net)
    
    return taches

def voir_taches(taches):
    if len(taches) == 0:
        print("il n'y a aucune tâche enregistréé")
    else:
        for num, t in enumerate(taches, start=1):
            print(f"{num}. {t}")
    return taches

def afficher_menu():
    print("Entrez 1 pour ajoutez une tâche ")
    print("Entrez 2 pour voir vos tâches ")
    print("Entrez 3 pour quiter ")
    choix = input("Ton choix ")
    return choix

while True: 
    #rendre taskmater maléable
    choix = afficher_menu()
    if choix == "1":
        ajouter_taches(taches)
    elif choix == "2":
         voir_taches(taches)
    elif choix == "3":
        print("A bientôt !")
        break
    else:
         print("Choix invalides")
    
    


