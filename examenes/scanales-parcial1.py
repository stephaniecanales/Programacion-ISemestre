#problema 1
def formarLista (num):
    if isinstance (num,int) and num > 0:
        return formarLista_aux (num)
    else:
        return "el numero no es correcto"

def formarLista_aux (num):
    if num == 1 :
        return []
    elif (num%10)%2 == 0:
        return [num%10] + formarLista_aux(num)
    else:
        return formarLista_aux (num)



#problema 2
def palidromo (num):
    if isinstance (num,int) and num > 0:
        return palidromo_aux (var,0)
    else:
        return "error"

def palidromo_aux (var,cont):
    if var == 0:
        return palidromo_comprobar (num,var)
    else:
        return palidromo_aux(var,cont+1) + var%10*10**cont

def palidromo_comprobar (num,var):
    if num == var:
        return True
    else:
        return False


#problema 3
def contarConsonantes (texto):
    if isinstance (texto, string):
        return consonante_aux (cadena)
    else:
        return "error"

def consonante_aux (cadena):
    if cadena == []:
        return 0
    elif cadena [0] == 'a' or cadena [0] == 'e' or cadena [0] == 'i' or cadena [0] == 'o' or cadena [0] == 'u':
        return consonante_aux (cadena [1:])
    else:
        return 1+ consonante_aux (cadena [1:])

#problema 4
def intercambiar (lista):
    if isinstance (lista, list):
        return intercambiar_aux (lista, 0)
    else:
        return "error"

def intercambiar_aux (lista, var):
    if lista == []:
        return []
    elif lista [[var]] %2 == 0:
        return lista [[var+1]] + intercambiar_aux (lista, var+1)
    else:
        return lista [[var-1]] + intercambiar_aux (lista, var+1)



