def longitud_digitos (valor):
    if isinstance (valor, int):
        return longitud_digitos_aux (valor)
    else:
        return "digite un numero entero"

def longitud_digitos_aux (valor) :
    if(valor == 0):
        return 0
    else:
        return 1 + longitud_digitos_aux(valor // 10)
    
