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

#Demande de taches de l'utilisateur

taches= input("Entrez votre tâches ")
taches_net = taches.strip().title()
print("✔️ Tâche enregistrée :", taches_net)
print("longueur :",len(taches_net))