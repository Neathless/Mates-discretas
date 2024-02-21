# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 19:53:44 2024

@author: Ricardo Lopez
"""

def es_numero_perfecto(numero):
    suma_divisores = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma_divisores += i
    return suma_divisores == numero

def numeros_perfectos_hasta_N(N):
    for numero in range(1, N + 1):
        if es_numero_perfecto(numero):
            print(numero)

# Solicitar al usuario el valor de N
N = int(input("Ingrese un valor : "))
numeros_perfectos_hasta_N(N)

