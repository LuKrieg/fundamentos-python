"""
Clase:        Clase 8
Tema:         Bloques iterativos
Ejercicio:    Adivina el numero
Descripción:  Adivina el numero generado aleatoriamente entre 1 y 100

Autor:        Lucy Fabiola Guerra Carranza
Fecha:        2025-05-31
Estado:       [ Terminado ]
"""
import random

print("5.4.1. ¡Adivina el número!")

numero_secreto = random.randint(1, 100)
adivinado = False

while not adivinado:
    intento = int(input("Ingresa un número entre 1 y 100: "))

    if intento < numero_secreto:
        print("El número secreto es mayor")
    elif intento > numero_secreto:
        print("El número secreto es menor")
    else:
        print(f"¡Felicidades! Has adivinado el número secreto: {numero_secreto}")
        adivinado = True

print("Fin del juego")
