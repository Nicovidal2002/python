from math import pi as PI_VALOR

#!/usr/bn/env python    --> Script python
# -*- coding: utf-8 -*- --> Codificacion utf8

__author__="Niko"

radio = int( input("Dime el primer numero:"))

perimetro = ((radio*2)*PI_VALOR)

print("Perimetro:", perimetro)

area = (PI_VALOR*radio**2)

print("Area:", area)