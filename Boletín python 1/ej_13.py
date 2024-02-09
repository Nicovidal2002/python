#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

radius = float(input("Ingrese el radio del cilindro: "))
height = float(input("Ingrese la altura del cilindro: "))

Volumen = round(math.pi * radius**2 * height, 3)

print(f"El volumen del cilindro con radio {radius} y altura {height} es", Volumen)
