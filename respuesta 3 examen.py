def zScore(lista, avg, s):
    if isinstance (lista,list) and isinstance (avg,float) and isinstance (s,float):
        return zScore_aux(lista,avg,s)
    else: return "Error"

def zScore_aux(lista,avg,s):
    if lista ==[]:
        return []
    else: return [(lista[0]-avg)/s]+zScore_aux(lista[1:],avg,s)
######con cola

def zScore2(lista, avg, s):
    if isinstance (lista,list) and isinstance (avg,float) and isinstance (s,float):
        return zScore_aux2(lista,avg,s,[])
    else: return "Error"

def zScore_aux2(lista,avg,s,result):
    if lista ==[]:
        return result
    else: return zScore_aux(lista[1:],avg,s,result+[(lista[0]-avg)/s])
