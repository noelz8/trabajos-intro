def rScore(Sx,Sy):
    if isinstance (Sx,list) and isinstance (Sy,list) and len(Sx)==len(Sy):
        return rScore_aux(Sx,Sy)/(len(Sx)-1)
    else: return "Error"

def rScore_aux(Sx,Sy):
    if Sx==[]:
        return 0
    else: return (Sx[0]*Sy[0])+rScore_aux(Sx[1:],Sy[1])

##cola
def rScore2(Sx,Sy):
    if isinstance (Sx,list) and isinstance (Sy,list) and len(Sx)==len(Sy):
        return rScore_aux2(Sx,Sy,0)/(len(Sx)-1)
    else: return "Error"

def rScore_aux2(Sx,Sy,result):
    if Sx==[]:
        return result
    else: return rScore_aux2(Sx[1:],Sy[1],result +(Sx[0]*Sy[0]))
