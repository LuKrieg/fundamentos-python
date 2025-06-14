"""
Clase:        10
Tema:         Manejo de matriz
Ejercicio:    10.3.1 Matriz simetrica
Descripción:  Determinar si matriz ingresada es simetrica o no
Autor:        Lucy Fabiola Guerra Carranza
Fecha:        2025-06-13
Estado:       [ Terminado ]
"""
print('10.3.1 Matriz simetrica')

def essimetrica(matriz):
    n = len(matriz)
    for i in range(n):
        for j in range(n):
            if matriz[i][j] != matriz[j][i]:
                return False
    return True

n = int(input("Ingrese la dimensión de la matriz: "))
matriz = []

print("Ingrese las filas de la matriz separando los elementos con comas:")
for _ in range(n):
    fila = list(map(int, input().split(',')))
    matriz.append(fila)

if essimetrica(matriz):
    print("La matriz es simétrica")
else:
    print("La matriz no es simétrica")
