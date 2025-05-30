"""
Clase:        Clase 6
Tema:         Manejo de listas
Ejercicio:    Ordenar una lista de números
Descripción:  Crear una linea con todos los números lideres

Autor:        Lucy Fabiola Guerra Carranza
Fecha:        2025-05-30
Estado:       [ Terminado ]
"""
a = list(map(int, input("Ingrese los números de su cadena de texto: ").split()))

lideres = []
max_derecha = float('-inf')

for num in reversed(a):
    if num > max_derecha:
        lideres.append(num)
        max_derecha = num

lideres.reverse()
print(*lideres)
