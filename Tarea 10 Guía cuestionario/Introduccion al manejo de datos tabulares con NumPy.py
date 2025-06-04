"""
Clase:        Clase 9
Tema:         Introducción al manejo de datos tabulares con NumPy
Ejercicio:    Cuestionario de trabajo
Descripción:  Aprender a manejar de manera eficiente los datos

Autor:        Lucy Fabiola Guerra Carranza
Fecha:        2025-06-03
Estado:       [ Terminado ]
"""
import numpy as np
consumo = np.array([
    [12.5, 13.2, 11.9, 14.0, 13.5, 15.0, 14.3],
    [10.1, 10.5, 10.0, 11.2, 11.5, 12.0, 11.8],
    [14.0, 14.2, 13.9, 15.5, 15.1, 16.0, 15.8],
    [9.0, 9.2, 8.9, 9.5, 9.8, 10.0, 9.7],
    [16.2, 16.5, 16.0, 17.1, 17.4, 18.0, 17.8],
    [11.0, 11.3, 11.1, 12.0, 12.4, 12.8, 12.5],
    [13.5, 13.8, 13.2, 14.1, 14.6, 15.0, 14.9],
    [10.8, 11.0, 10.6, 11.5, 11.8, 12.2, 12.0],
    [15.1, 15.5, 15.0, 16.0, 16.4, 17.0, 16.7],
    [8.5, 8.7, 8.4, 9.0, 9.2, 9.5, 9.3],
])

# 2. Exploración inicial de los datos

print("Dimensiones:", consumo.ndim)
print("Forma:", consumo.shape)
print("Tipo de datos:", consumo.dtype)
print("Consumo primer hogar:", consumo[0])
print("Consumo el miércoles (día 3):", consumo[:, 2])

# 3. Introducción al Análisis Estadístico

# Promedio por hogar
promedio_por_hogar = np.mean(consumo, axis=1)
# Promedio por día
promedio_por_dia = np.mean(consumo, axis=0)
# Suma total
total_consumo = np.sum(consumo)

print(promedio_por_hogar)
print(promedio_por_dia)
print(total_consumo)

# Máximo por hogar
maximos = np.max(consumo, axis=1)
# Mínimo por día
minimos = np.min(consumo, axis=0)
# Desviación estándar global
desviacion = np.std(consumo)

print(maximos)
print(minimos)
print(desviacion)

# Comparación de hogares
consumo_total_hogar = np.sum(consumo, axis=1)
hogar_mayor_consumo = np.argmax(consumo_total_hogar)
hogar_mas_eficiente = np.argmin(consumo_total_hogar)

print(consumo_total_hogar)
print(hogar_mayor_consumo)
print(hogar_mas_eficiente)

# 4. Transformaciones y Filtros

# Hogares con consumo > 100
altos = consumo_total_hogar > 100
consumo_mayor_100 = np.where(altos)[0]
print(f"Ids de hogares con consumo mayor a 100: {consumo_mayor_100}")

# Normalización Min-Max
consumo_normalizado = (consumo - consumo.min()) / (consumo.max() - consumo.min())
print(consumo_normalizado)

# --------------------------------------------
# 5. Cuestionario de Trabajo
# --------------------------------------------

# 1. Consumo del hogar 5 el viernes (día 5)
consumo_viernes_hogar5 = consumo[4, 5]
print(f"Consumo del hogar 5 el viernes: {consumo_viernes_hogar5} kWh")

# 2. Consumo de los últimos 3 hogares el domingo
consumo_domingo_ultimos3 = consumo[-3:, 6]
print("Consumo de los últimos 3 hogares el domingo:", consumo_domingo_ultimos3)

# 3. Promedio de consumo los fines de semana (sábado y domingo)
consumo_finde = consumo[:, 5:7]
promedio_finde = np.mean(consumo_finde)
print(f"Promedio de consumo en fines de semana: {promedio_finde:.2f} kWh")

# 4. Día con mayor desviación estándar
desviacion_por_dia = np.std(consumo, axis=0)
dia_mayor_desviacion = np.argmax(desviacion_por_dia)
print("Desviaciones estándar por día:", desviacion_por_dia)
print(f"Día de mayor desviación estándar: {dia_mayor_desviacion} (0=Lunes, ..., 6=Domingo)")

# 5. 3 hogares con menor consumo semanal
total_por_hogar = np.sum(consumo, axis=1)
indices_menor_consumo = np.argsort(total_por_hogar)[:3]
valores_menor_consumo = total_por_hogar[indices_menor_consumo]
print("Índices de los 3 hogares con menor consumo:", indices_menor_consumo)
print("Valores de consumo total de esos hogares:", valores_menor_consumo)

# 6. Aumento del 10% del hogar 3
nuevo_consumo_hogar3 = consumo[2] * 1.10
total_nuevo_hogar3 = np.sum(nuevo_consumo_hogar3)
print(f"Nuevo consumo total del hogar 3 con aumento del 10%: {total_nuevo_hogar3:.2f} kWh")
