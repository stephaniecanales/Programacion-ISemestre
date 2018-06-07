def primos_lista (lista):
    if isinstance (lista, list):
        return listaprimo(lista)
    else:
        return "error"

def listaprimo(lista):
    if lista == []:
        return []
    elif numero_primo (lista[0], lista[0]-1) == True:
        return [lista [0]] + listaprimo(lista[1:])
    else:
        return listaprimo (lista [1:])

    
def numero_primo(num, divisor):
    if num == 1 or num == 1 or num == 2 or num ==3 :
        return True
    elif divisor == 1:
        return True
    elif num % divisor == 0:
        return False
    else: return numero_primo (num , divisor -1)
