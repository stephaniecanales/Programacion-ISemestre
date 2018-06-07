#encontrar el valor minimo y maximo de la lista

def minimo_maximo(lista):
    #if type(lista) == list
    if isinstance(lista,list):
        return menor (lista), mayor (lista)
    else:
        return "Error: el valor ingresado no es una lista"

def menor(lista):
    if len (lista) == 1:
        return lista [0]
    elif lista [0] < lista [1]:
        return menor([lista[0]]+lista[2:])
    else:
        return menor (lista[1:])


def mayor(lista):
    if len (lista) == 1:
        return lista [0]
    elif lista [0] > lista [1]:
        return mayor([lista[0]]+lista[2:])
    else:
        return mayor (lista[1:])
