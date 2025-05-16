'''
Clase:        Clase 1
Tema:         Ejercicio de exploración 2
Ejercicio:    Contraseña de 8 caracteres
Descripción:  Uso básico de variables y operaciones de desigualdades en Python.

Autor:        Lucy Fabiola Guerra Carranza
Fecha:        2025-05-16
Estado:       [ Terminado ]
'''
#Calcular el impuesto a pagar por consumo de energía
#Si consume de 0 a 100 unidades, no hay impuestos
#Si son de 101 a 200, son $0.5 por cada unidad
#Si son 201 o más unidades, son $0.7 por cada unidad

x = int(input("Ingrese las unidades consumidas: "))

if x <= 100:
    print("Sin impuestos")
elif x == 101 or x <= 200:
    presu1 = x * (1/2)
    print("Debe pagar " + str(presu1))
elif x >= 201:
    presu2 = x * (7/10)
    print("Debe de pagar " + str(presu2))
