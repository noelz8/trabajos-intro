##################practica 1
def pares(num):
    if isinstance (num,int)and num !=0:
        return pares_aux(num)
    else: return "Error"

def pares_aux(num):
    if num==0:
        return []
    elif num%10%2==0:
        return pares_aux(num//10)+[num%10] 
    else: return pares_aux(num//10)
##practica 2

def palindromo(palin):
    if isinstance (palin,int) and palin !=0:
        return palin_aux(palin,pal2)
    else: return "Error"

def palin_aux(palin,pal2):
    if (palin,pal2) ==0:
        return False
    if palin==pal2:
        return palin_aux(palin,pal2)
    
        
