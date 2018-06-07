"""Dada una lista de numeros, buscar un numero especifico
en las lista y borrarlo"""
def elimNumero (lista,num):
    if isinstance (lista,list) and (num,int):
        return nuevaLista(lista,num)
    else:
        return "Error"
def nuevaLista(lista,num):
    if lista == []:
        return [ ] #devuelve una lista vacia y a esta le agrega las listas que encontro
    elif lista [0] == num:
        return nuevaLista(lista[1: ],num)
    else:
        return [lista[0]]+nuevaLista(lista[1: ],num) 


