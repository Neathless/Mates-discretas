# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 21:05:03 2024

@author:Ricardo Lopez
"""

def suma_divisores_propios(numero):
    suma = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma += i
    return suma

def son_amigos(numero1, numero2):
    return suma_divisores_propios(numero1) == numero2 and suma_divisores_propios(numero2) == numero1
    
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

if son_amigos(numero1, numero2):
    print(f"{numero1} y {numero2} son números amigos.")
else:
    print(f"{numero1} y {numero2} no son números amigos.")
