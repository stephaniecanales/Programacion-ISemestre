def mult_matrices (matriz1,matriz2):
    if isinstance (matriz1,list) and (matriz2,list) and len(matriz1)== len(matriz2[0]):
        return mult_aux(matriz1,matriz2,0,0,[],0)
    else:
        return "error"

def mult_aux (matriz1,matriz2,fila,columna,resultado,suma):
    if fila == len(matriz1):
        return resultado
    elif columna == len(matriz1[0]):
        return mult_aux(matriz1,matriz2,fila+1,0,resultado+[suma],0)
    else:
        return mult_aux(matriz1,matriz2,fila,columna+1,resultado, suma + matriz1[fila][columna] * matriz2[columna][fila])
