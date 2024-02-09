#!/usr/bn/env python    --> Script python
# -*- coding: utf-8 -*- --> Codificacion utf8

__author__ = "Niko"

try:
    num1 = int(input("Escribe el primer numero: "))
    num2 = int(input("Escribe el segungo numero: "))

    sum = num1 + num2

    if sum > 10:
        print("La suma es mayor de 10.")
    else:
        print("La suma es menor de 10.")
except ValueError:
    print("Error: Ingrese solo números enteros.")
        

