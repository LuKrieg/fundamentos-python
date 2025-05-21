"""
Clase:        Clase 1
Tema:         Ejercicio de exploración 1.2
Ejercicio:    Creación de correo
Descripción:  Uso básico de variables y operaciones de desigualdades en Python.

Autor:        Lucy Fabiola Guerra Carranza
Fecha:        2025-05-20
Estado:       [ Terminado ]
"""

ncompleto = input("Ingrese su nombre completo (dos nombres y dos apellidos): ")
partes = ncompleto.strip().split()

pnombre = partes[0].lower()
papellido = partes[2].lower()

email = pnombre + "." + papellido + "@keyinstitute.edu.sv"

print("El correo que se debe asignar al usuario ingresado es: " + email)
