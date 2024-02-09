#!/usr/bn/env python    --> Script python
# -*- coding: utf-8 -*- --> Codificacion utf8

__author__="Niko"

nombre, apellido = "Niko", "Vidal"

print(nombre, apellido)

print("Hola, me llamo {} y me apellido{}".format(nombre, apellido))
print("Hola, me llamo {nombre} y me apellido{apellido}")

cadena = "hola"
print(len(cadena))
print(cadena.capitalize())
print(cadena.upper)
print(cadena.count("a"))
print(type(cadena))
print(cadena.isnumeric())
print(cadena.upper().isupper())
print("Ho" == "ho")
print(cadena[-1])
print(cadena[-2])
print(cadena[-3])
print(cadena[-4])

cadena2 = "hola, a todos"
print(cadena2.split())
print(cadena2.split(","))

nombre_2 = (input("Dime tu nombre:"))
print(nombre_2)

numero = int (input("Dime un numero:"))
print(numero+3)


