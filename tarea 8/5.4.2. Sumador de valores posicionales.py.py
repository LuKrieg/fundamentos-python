"""
Clase:        Clase 8
Tema:         Bloques iterativos
Ejercicio:    Suma de valores posicionales
Descripción:  Suma de numero que ingresa el usuario hasta que solo quede uno

Autor:        Lucy Fabiola Guerra Carranza
Fecha:        2025-05-31
Estado:       [ Terminado ]
"""
print("Sumador de valores posicionales")

numero = int(input("Ingresa un número: "))
print("Proceso de reducción para", + numero, ": ")

while numero >= 10:
    suma = 0
    for digito in str(numero):
        suma += int(digito)
    print(f"{numero} = {suma}")
    numero = suma

print(f"El resultado final es: {numero}")
