def numeros_pares (num):
    if isinstance (num, int) and (num >= 1): 
        return numeros_pares_aux (num), numeros_impares_aux (num)
    else:
        return "Digíte un número válido"


def numeros_pares_aux (num):
    if num == 0:
        return 0
    elif ((num % 10) %2) == 0:
        return 1 + numeros_pares_aux (num // 10)
    else:
        return numeros_pares_aux (num // 10)
    
def numeros_impares_aux (num):
    if num == 0:
        return 0
    elif ((num % 10) %2) == 1:
        return 1 + numeros_impares_aux (num // 10)
    else:
        return numeros_impares_aux (num // 10)
    
