def averiguar_binario(dig):
    if isinstance (dig, int):
        return binario_aux(dig)
    else:
        return "error"

def binario_aux (dig):
    if dig == 1:
        return "1"
    elif dig%2 == 0:
        return binario_aux(dig//2) + "0"
    else:
        return binario_aux(dig//2) + "1"
    
        
    


