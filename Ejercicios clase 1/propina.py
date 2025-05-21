"""
Clase:        Clase 1
Tema:         Ejercicio de exploración 1.1
Ejercicio:    Generador de propina
Descripción:  Uso básico de variables y operaciones de desigualdades en Python.

Autor:        Lucy Fabiola Guerra Carranza
Fecha:        2025-05-20
Estado:       [ Terminado ]
"""

cuenta = float(input("Ingrese el total a cancelar: $"))

porcentaje = float(input("Ingrese el porcentaje de propina: "))

propina = (cuenta * porcentaje) /  100
tpropina = cuenta + propina

print("Total de la cuenta: $" + str(cuenta))
print("Propina: $" + str(propina))
print("Total de la cuenta con propina(" + str(porcentaje) + "%): $" + str(tpropina))
