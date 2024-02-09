#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Niko"

a = float(input("Ingrese el coeficiente a: "))
b = float(input("Ingrese el coeficiente b: "))
c = float(input("Ingrese el coeficiente c: "))

solucion_1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
solucion_2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)

print("Las soluciones de la ecuación son:")
print("Solución 1:", solucion_1)
print("Solución 2:", solucion_2)
