def valor_factorial (valor):
    if isinstance (valor, int) and (valor> 0):
        return valor_factorial_aux (valor)
    else:
        return "no hay factorial"

def valor_factorial_aux (valor):
    if valor == 0:
        return 1
    else:
        return valor * valor_factorial_aux(valor-1)
