'''
Clase:        Clase 1
Tema:         Ejercicio de exploración 1
Ejercicio:    Contraseña de 8 caracteres
Descripción:  Uso básico de variables y operaciones de desigualdades en Python.

Autor:        Lucy Fabiola Guerra Carranza
Fecha:        2025-05-16
Estado:       [ Terminado ]
'''


#Solicita una cadena de texto que representa una contraseña.
# verifica si la contraseña cumple con las siguiente condiciones al tener al menos
# 8 caracteres, un número y una mayúscula

x = input("Escriba su contraseña: ")

if len(x) >= 8:
    print("Contraseña segura")
else:
    print("La contraseña no es segura")
