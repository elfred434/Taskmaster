# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 08:23:55 2026

@author: elfre
"""

def est_premier(n):
    i = 0
    
    if n < 2:
        return False
    
    for i in range (2, n):
        if n % i == 0:
            return False
        
    return True

n = int(input("Entrez le nombre"))


for j in range (2,n+1):
    if est_premier(j) == True:
        print(j)
        
    
