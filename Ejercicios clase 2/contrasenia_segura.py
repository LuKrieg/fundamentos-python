'''
Clase:        Clase 2
Tema:         Ejercicio de exploración 2.1
Ejercicio:    Contraseña de 8 caracteres
Descripción:  Uso básico de variables y operaciones de desigualdades en Python.

Autor:        Lucy Fabiola Guerra Carranza
Fecha:        2025-05-16
Estado:       [ Terminado ]
'''

x = input("Escriba su contraseña: ")

long = len(x) >= 8
mayus = any(letra.isupper() for letra in x)
num = any(caracter.isdigit() for caracter in x)

if long and mayus and num:
    print("Contraseña segura")
else:
    print("La contraseña no es segura")
