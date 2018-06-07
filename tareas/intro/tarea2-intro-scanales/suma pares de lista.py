#suma de los valores pares de una lista


#con indice y recursion de cola

def suma_pares(lista):
    #if type(lista) == list
    if isinstance(lista,list):
        return suma_pares_aux (lista,0,0)
    else:
        return "Error: el valor ingresado no es una lista"

def suma_pares_aux(lista,indice,suma):
    if indice == len(lista):
        return suma
    elif lista [indice] % 2 == 0:
        return suma_pares_aux(lista,indice+1,suma+lista[indice])
    else:
        return suma_pares_aux(lista, indice+1, suma)


#suma de los valores pares de una lista

#con slice y recursion de pila

def suma_pares(lista):
    #if type(lista) == list
    if isinstance(lista,list):
        return suma_pares_aux (lista)
    else:
        return "Error: el valor ingresado no es una lista"

def suma_pares_aux(lista):
    if lista == []:
        return 0
    elif lista [0] % 2 == 0:
        return lista [0]+suma_pares_aux(lista[1:])
    else:
        return suma_pares_aux(lista[1:])
