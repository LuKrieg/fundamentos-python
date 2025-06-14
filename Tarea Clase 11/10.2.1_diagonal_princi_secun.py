"""
Clase:        10
Tema:         Manejo de matriz
Ejercicio:    10.2.1 Diagonal principal y secundaria
Descripción:  Extrae los elementos de la diagonal principal (de izquierda a derecha) y la diagonal secundaria (de derecha a izquierda) de una matriz cuadrada dada por el usuario.
Autor:        Lucy Fabiola Guerra Carranza
Fecha:        2025-06-13
Estado:       [ Terminado ]
"""
print('10.2.1 Diagonal principal y secundaria')

n = int(input("Ingrese la dimensión de la matriz (N): "))
print("Ingrese las filas separando los números con comas:")

matriz = []
for _ in range(n):
    fila = list(map(int, input().split(',')))
    matriz.append(fila)

diagonal_principal = [matriz[i][i] for i in range(n)]
diagonal_secundaria = [matriz[i][n - 1 - i] for i in range(n)]

print(diagonal_principal)
print(diagonal_secundaria)
