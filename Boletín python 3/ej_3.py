#!/usr/bn/env python    --> Script python
# -*- coding: utf-8 -*- --> Codificacion utf8

__author__="Niko"

number = float(input("Escribe un numero: "))

try:
    if number >= 10 and number <= 100:
        print("El número está entre 10 y 100.")
    else:
        print("El número no está entre 10 y 100.")
except ValueError:
    print("Entrada inválida. Por favor, ingresa un valor numérico.")
