# 1. Crear una matriz de 5x5 inicializada con ceros
# Usamos una lista de listas
matriz = [[0 for _ in range(5)] for _ in range(5)]

print("--- Ingreso de datos para la matriz 5x5 ---")

# 2. Bucle anidado para pedir los datos
for fila in range(5):
    for columna in range(5):
        # Pedimos el número y lo convertimos a entero (int)
        valor = int(input(f"Ingrese el valor para la posición [{fila}][{columna}]: "))
        matriz[fila][columna] = valor

print("\nMatriz ingresada:")

# 3. Bucle anidado para mostrar la matriz en forma de tabla
for fila in range(5):
    for columna in range(5):
        # end="\t" mantiene el cursor en la misma línea con una tabulación
        print(matriz[fila][columna], end="\t")

    # Al terminar cada fila, imprimimos un salto de línea vacío
    print()