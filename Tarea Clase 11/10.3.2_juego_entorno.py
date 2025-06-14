"""
Clase:        10
Tema:         Manejo de matriz
Ejercicio:    10.3.2 Juego del entorno
Descripción:  cuenta cuántos unos hay alrededor de cada celda en una matriz binaria, considerando todas las direcciones (vertical, horizontal y diagonales)
Autor:        Lucy Fabiola Guerra Carranza
Fecha:        2025-06-13
Estado:       [ Terminado ]
"""
print('10.3.2 Juego del entorno')


def contar_vecinos(cuadricula, filas, columnas):
    resultado_total = []

    # Posibles direcciones (vecinos en 8 direcciones)
    movimientos_vecinos = [
        (-1, -1), (-1, 0), (-1, 1),  # arriba-izquierda, arriba, arriba-derecha
        (0, -1),           (0, 1),   # izquierda,        derecha
        (1, -1),  (1, 0),  (1, 1)    # abajo-izquierda,  abajo,  abajo-derecha
    ]

    for fila_actual in range(filas):
        fila_contador = []
        for columna_actual in range(columnas):
            vecinos_activos = 0
            for mov_fila, mov_col in movimientos_vecinos:
                vecino_fila = fila_actual + mov_fila
                vecino_columna = columna_actual + mov_col
                if 0 <= vecino_fila < filas and 0 <= vecino_columna < columnas:
                    if cuadricula[vecino_fila][vecino_columna] == 1:
                        vecinos_activos += 1
            fila_contador.append(vecinos_activos)
        resultado_total.append(fila_contador)

    return resultado_total

n = int(input("Ingrese número de filas (N): "))
m = int(input("Ingrese número de columnas (M): "))
print("Ingrese la matriz fila por fila, separando los números con comas:")

matriz = []
for _ in range(n):
    fila = list(map(int, input().split(',')))
    matriz.append(fila)

resultado = contar_vecinos(matriz, n, m)

print("Resultado:")
for fila in resultado:
    print(fila)
