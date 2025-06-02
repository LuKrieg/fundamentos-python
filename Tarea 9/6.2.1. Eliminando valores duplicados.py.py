"""
Clase:        Clase 6
Tema:         Manejo de listas
Ejercicio:    Eliminar valores duplicados
Descripción:  De una cadena de texto convertirla en lista y eliminar sus duplicados
Autor:        Lucy Fabiola Guerra Carranza
Fecha:        2025-05-30
Estado:       [ Terminado ]
"""
a = list(map(int, input("Ingrese los números (con división de espacio): ").split()))

nums = []
resultado = []

for num in a:
    if num not in nums:
        resultado.append(num)
        nums.append(num)

print(*resultado)
