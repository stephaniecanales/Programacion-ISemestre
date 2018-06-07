import math
def sumatoria (lista):
  if isinstance (lista, list):
    return sumatoria_aux(lista)
  else:
    return "error"

def sumatoria_aux (lista):
  if lista == []:
      return 0
  else:
      return lista[0] + sumatoria_aux(lista[1:])
