#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Niko"

kilometros_recorridos = float(input("Ingrese el número de kilómetros recorridos: "))
consumo_litros = float(input("Ingrese el consumo del coche en litros cada 100 kilómetros: "))
precio_combustible = float(input("Ingrese el precio en euros de un litro de combustible: "))

costo_viaje = (kilometros_recorridos / 100) * consumo_litros * precio_combustible

print("El costo del viaje es:", costo_viaje, "euros")
