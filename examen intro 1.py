####Pregunta 1
def combinacion(hp,dell):
    if isinstance (hp,list) and isinstance (dell,list):
        return combinaciones_aux(hp,dell)
    else: return "Error"

def combinaciones_aux(hp,dell):
    if [hp+dell]=[]
    return [hp[0]+dell[0]+combinaciones_aux(hp[:-1],dell[:-1]
####Pregunta 2
import.math
def std(lista,avg):
    if isinstance (lista,list) and (avg,int):
        return std_aux(lista,avg,0)
    else: return "Error"

def std_aux(lista,avg,sumat):
    if math.sqrt(sumat)==0:
        return 0
    elif ((lista[0]-avg)**2)+std_Aux(lista[:-1],avg,sumat)=0:
        return std_aux(lista,avg,sumat+(lista[0:]-avg)**2)
    elif sumat//10+std_aux(lista,avg,sumat):
        return std_aux(lista,avg,sumat//10)
    elif math.sqrt(sumat)+std_aux(lista,avg,sumat):
        return std_aux(lista,avg,math.sqrt(sumat))
    else:
        return std_aux(lista,avg,sumat)

####Pregunta 3
def zScore(listaX,S,avg):
    if isinstance (listaX,list) and isinstance (S,int) and isinstance (avg,int):
        return zScore_aux(listaX,S,avg)
    else: return "Error"

def zScore_aux(listaX,S,avg):
    if (listaX-avg)//S=[]:
        return []
    elif (lista X[0:]-avg)+zScore_aux(listaX[:-1],S,avg):
        return zScore_aux(listaX,S,avg)
    elif (listaX-avg)//S+zScore_aux(listaX,avg):
        return zScore_aux(listaX,S,avg)
####Pregunta 4
def rScore(Zx,Zy):
    if isinstance (Zx,list) and (Zy,list) and len(Zx,list)=len(Zy,list):
        return rScore_aux(Zx,Zy,0)
    else: return "Error"

def rScore_aux(Zx,Zy,result):
    if result//(len(Zx)-1)==[]:
        return 0
    elif (Zx[0]*Zy[0])+rScore_aux(Zx[-1:],Zy[-1:],resutl):
        return rScore_aux(Zx,Zy,resutl+(Zx[0:]*Zy[0:]))
    elif (result//(len(Zx)-1)+rScore_aux(Zx,Zy,result):
          return rScore_aux(Zx,Zy,result//len(Zx)-1)
          else: return rScore_aux(Zx,Zy,result)
