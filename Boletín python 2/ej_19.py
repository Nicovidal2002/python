#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Niko"

tareas = float(input("Ingrese la nota de tareas (0-10): "))
examen_teórico = float(input("Ingrese la nota del examen teórico (0-10): "))
examen_práctico = float(input("Ingrese la nota del examen práctico (0-10): "))

nota_final = (tareas * 0.15) + (examen_teórico * 0.20) + (examen_práctico * 0.65)

print("Su nota final es:", nota_final)
