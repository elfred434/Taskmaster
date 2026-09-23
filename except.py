# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 14:07:54 2026

@author: elfre
"""

def demande_entier(mess):
    while True:
        try:
            return int(input(mess))
        except ValueError:
            print("Please , enter a nomber integrer")
            
n = demande_entier("Enter a integrer nombre")
print(f"the nomber is {n}")