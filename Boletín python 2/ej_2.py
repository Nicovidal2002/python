#!/usr/bn/env python    --> Script python
# -*- coding: utf-8 -*- --> Codificación utf8

__author__="Niko"

number = float(input("Escribe un numero: "))

try:
    if number > 0:
        print("El número es positivo.")
    elif number < 0:
        print("El número es negativo.")
    else:
        print("El número es igual a cero.")
                
except ValueError:
    print("Entrada inválida. Por favor, ingresa un valor numérico.")





