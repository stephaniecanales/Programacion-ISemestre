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





def averiguar_decimal (num):
    if isinstance (num, int):
        return decimal_aux(num,0)
    else: return "error"
    
def decimal_aux(num, cont):
    if num == 0:
        return 0
    elif num%10 == 1 or num%10 == 0:
        return (num%10)*2**cont + decimal_aux(num//10,cont+1)
    else: return "error"
        
    
        
    


