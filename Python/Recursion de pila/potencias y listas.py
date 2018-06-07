def potencia_suma (lista):
    if isinstance (lista, list):
        return suma_aux (lista,1)
    else:
        return "error"

def suma_aux (lista, cont):
    if lista == []:
        return 0
    elif isinstance (lista[0], list):
        return suma_aux (lista[0] + lista[1:],cont)
    else:
        return lista [0]**(cont) + suma_aux (lista[1:], cont+1)
