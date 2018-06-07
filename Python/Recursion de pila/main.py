
def sumatoria (n):
  if n == 0:
    return 0
  else:
    return producto (n) + sumatoria (n-1)
    
def producto (j):
  if j == 0:
    return 1
  else:
    return (3*j **2 - j) * producto(j-1)