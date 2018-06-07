def invertir(lista):
    if isinstance (lista,list):
        return invertir_aux(lista,lista[indice],0)
    else:
        return "error"

def invetir_aux(lista,posicion,indice):
    if indice == len(lista):
        return lista
    else:
        return invertir_aux(lista,lista-[indice+1], indice+1)





###########################################################################################




def consecutivos (n,matriz):
    if isinstance (n,int) and (matriz,lista) and len(matriz)=len(matriz[0]):
        return consecutivos_aux(n, matriz, len(matriz),len(matriz[0],0,0,1)
    else:
        return "error"

def consecutivos_aux(n, matriz, cant_filas, cant_colum, fila,columna, indice):
    if fila == cant_filas and indice != n**2:
        return False
    if columna == cant_colum:
        return consecutivos_aux(n,matriz,cant_filas,cant_colum,fila+1,0,indice)
    elif matriz[fila][columna] == indice:
        return consecutivos_aux(n,matriz,cant_filas,cant_colum,fila,columna+1,indice+1)
    else:
        return consecutivos_aux(n,matriz,cant_filas,cant_colum,fila,columna+1,indice)
    elif indice == n**2:
        return True


###############################################################################################


def es_magico (matriz):
    if isinstance (matriz,list):
        return aux(matriz,len(matriz),len(matriz[0]),0,0,[],[])
    else:
        return "error"


def aux (matriz,cant_filas,cant_colum,fila,columna,suma,nueva):
    if nueva // cant_filas == suma:
        return diagonal
    elif columna == cant_colum:
        return aux(matriz,cant_filas,cant_colum,fila+1,[],nueva+suma)
    elif fila < cant_filas:
        return aux(matriz,cant_filas,cant_colum,fila,columna+1,suma+ matriz[fila][columna],nueva)
    if nueva // cant_filas != suma:
        return False

##############################################################################################


def rotar (matriz):
    if isinstance (matriz,list):
        return rotar_aux(matriz,len(matriz),len(matriz[0]),0,0,[],[])
    else:
        return "error"

def rotar_aux (matriz, cant_filas,cant_colum,indice1,indice2,matriz1,matriz2):
    if




















