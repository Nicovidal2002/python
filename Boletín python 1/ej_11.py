#!/usr/bn/env python    --> Script python
# -*- coding: utf-8 -*- --> Codificacion utf8

__author__="Niko"

SalarioB = int( input("Cual es tu salario bruto"))
Calc = int( input("Cual es tu IRPF"))

IRPFcalc = Calc/100

SalarioN = (SalarioB - (SalarioB * IRPFcalc))

print(round(SalarioN, 2))