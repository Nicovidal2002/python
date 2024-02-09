#!/usr/bn/env python    --> Script python
# -*- coding: utf-8 -*- --> Codificacion utf8

__author__="Niko"

try:
    numero = int(input("Introduce un número: "))
    if numero % 2 == 0:
        print("El número es par")
    else:
        print("El número es impar")
except ValueError:
    print("Error: Debes introducir un valor numérico")

