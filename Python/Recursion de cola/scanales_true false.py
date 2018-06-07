def true_false (num):
    if isinstance (num, int) and (num >= 0):
        return true_false_aux (num)
    else:
        return "Error"

def true_false_aux (num):
    if num == 0:
        return True
    elif ((num % 10) >= 0) and ((num % 10) <= 4):
        return true_false_aux(num  // 10)
    else:
        return False 
