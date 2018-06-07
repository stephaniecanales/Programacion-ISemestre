def suma_matriz(elem, matriz):
    if isinstance(matriz, list) and matriz != [] and isinstance(elem, int):
        return matriz_aux(elem, matriz, len(matriz), len(matriz[0]), 0, 0,[],[])
    else: return "Error"

def matriz_aux(elemento, matriz, num_filas, num_columnas, fila, columna,suma,f):
    if fila == num_filas:
        return suma
    elif columna == num_columnas:
        return matriz_aux(elemento, matriz, num_filas, num_columnas, fila + 1, 0, suma + [f], [])
    else: return matriz_aux(elemento, matriz, num_filas, num_columnas, fila, columna + 1, suma, f + [matriz[fila][columna] + elemento])
