# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 08:00:26 2026

@author: elfre
"""

note = float(input("Entrez un votre note"))

if note <10:
    print("Recalé")
elif note < 12:
    print("Passable")
elif note < 14:
    print("Assez bien")
elif note < 16:
    print("Bien")
else:
    print("Très bien")
