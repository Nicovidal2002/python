#!/usr/bin/env python    # Script python
# -*- coding: utf-8 -*- # Codificación utf8

__author__ = "Niko"

def comprobar_valores_iguales(num1, num2, num3):
    if num1 == num2 or num1 == num3 or num2 == num3:
        print("Error: Los números introducidos no pueden ser iguales.")
    else:
        return calcular_menor_numero(num1, num2, num3)

def calcular_menor_numero(num1, num2, num3):
    if num1 < num2 and num1 < num3:
        return num1
    elif num2 < num1 and num2 < num3:
        return num2
    else:
        return num3


num1 = (input("Introduce el primer número: "))
num2 = (input("Introduce el segundo número: "))
num3 = (input("Introduce el tercer número: "))


if comprobar_valores_iguales(num1, num2, num3):
    menor_numero = calcular_menor_numero(num1, num2, num3)
    print("El menor número es:", menor_numero)
