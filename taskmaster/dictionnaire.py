# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 09:52:30 2026

@author: elfre
"""
"""
perso = {"nom": "Elfred", "ville": "Porto-Novo", "age": 20}
for cle, valeur in perso.items():
    print(f"{cle} -> {valeur}")"""
    
annuaire = {}
for i in range(2):
    nom = input("Entrez le nom ")
    tel = input("Entre le tel ")
    annuaire[nom] = tel

for cle, valeur in annuaire.items():
    print(f"{cle} -> {valeur}")