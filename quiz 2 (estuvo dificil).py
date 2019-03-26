def palindromo(palin):
    if isinstance (palin,list)==len(palin):
        return palin_aux(pal1,pal2)
    else: return "Error"

def palin_aux(pal1,pal2):
    if (pal1[0:], pal2[0:]==[]):
        return False
    if pal1[0]==pal2[-1]:
        return pali_aux(pal1[1],pal2[-1])
    

def promedio (num, largo):
    if isinstance num(list, int) and isinstance largo(int) and num== len(largo):
        return prom_aux(num,largo)
    else: return "Error"

def prom_aux(num/largo):
    if (num[0] + num[1]==[]):
        return []
    else:
        return prom_aux(num[0:]+num[-1]/largo)
                        

