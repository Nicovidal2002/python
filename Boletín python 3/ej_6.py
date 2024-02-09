#!/usr/bn/env python    --> Script python
# -*- coding: utf-8 -*- --> Codificacion utf8

__author__="Niko"

try:
    num1 = int(input("Introduce el primer número: "))
    num2 = int(input("Introduce el segundo número: "))
    
    if num1 % num2 == 0:
        print("El primer número es divisor del segundo.")
    elif num2 % num1 == 0:
        print("El segundo número es divisor del primero.")
    else:
        print("Ninguno de los dos números es divisor del otro.")
except ValueError:
    print("Error: Debes introducir un valor numérico, intentalo de nuevo")

