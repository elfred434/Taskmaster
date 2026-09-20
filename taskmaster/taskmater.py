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
while True:
    tache= input("Entrez votre tâches ")
    taches_net = tache.strip().title()
    taches.append(taches_net)
    if tache.lower().strip() == "stop":
        
        break
print("✔️ Tâche enregistrée :", taches_net)
print("longueur :",len(taches_net))
print(f"Tu as maintenant {len(taches)} tâches(s)")
for num, t in enumerate(taches, start=1):
    print(f"{num}. {t}")
    
    
    


