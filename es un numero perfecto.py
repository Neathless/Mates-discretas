# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 19:45:07 2024

@author: Ricardo Lopez
"""

numero = int(input("Ingresa un numero:"))

suma_divisores = 0


for i in range(1, numero):
    if numero % i == 0:
        suma_divisores += i


if suma_divisores == numero:
    print(f" El número {numero} es perfecto")
else:
    print(f" El número {numero} no es perfecto.")

