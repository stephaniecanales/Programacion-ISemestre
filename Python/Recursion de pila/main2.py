def suma (x):
  if isinstance (x, int) and x >= 1:
    return suma_aux(x)
  else:
    return "error"
    
def suma_aux (x):
  if x == 0:
    return 0
  else:
    return (x + 5 *((x*x)**2)) + suma_aux (x-1)