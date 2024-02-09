#!/usr/bn/env python    --> Script python
# -*- coding: utf-8 -*- --> Codificacion utf8

__author__ = "Niko"
try:
    numero1 = float(input("Introduce el primer número: "))
    numero2 = float(input("Introduce el segundo número: "))
    numero3 = float(input("Introduce el tercer número: "))

    if numero1 == numero2 or numero1 == numero3 or numero2 == numero3:
        print("Error: Los números deben ser diferentes.")
    else:
        if numero1 > numero2 and numero1 > numero3:
            print("El número mayor es el primero.")
        elif numero2 > numero1 and numero2 > numero3:
            print("El número mayor es el segundo.")
        else:
            print("El número mayor es el tercero.")

except ValueError: 
    print("Error: Debes introducir un valor numérico, intentalo de nuevo")
    
    

    
