# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 18:32:22 2024

@author:Ricardo Lopez
"""

def triangulo_pascal(filas):
    fila = [1]
    cero = [0]
    
    for _ in range(filas):
        print(fila)
        
        fila = [i + d for i, d in zip(fila + cero, cero + fila)]
   
triangulo_pascal(5) 