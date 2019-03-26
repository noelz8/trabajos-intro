def suma(num):
    if isinstance(num, int):
        if num == 0:
            return 0
        else:
            return num%10 + suma(num//10)
    else:
        return "Error"
    
