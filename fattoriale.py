import sys
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)
numero = int(input("Inserisci un numero "))
print(f"Il fattoriale del numero inserito è {fact(numero)}")
print(sys.version)