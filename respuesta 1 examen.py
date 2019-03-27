######1
hp=["h1","h2","h3"]
dell=["d1","d2"]
def combinaciones(hp,dell):
    if isinstance (hp,list) and isinstance (dell,list) and len(hp)>0 and len(dell)>0:
        return combinaciones_aux(hp,dell)
    else: return "Error"

def combinaciones_aux(hp,dell):
    if hp==[]:
        return []
    else: return comb_aux(hp[0],dell) + combinaciones_aux(hp[1:],dell)

def comb_aux(valor, dell):
    if dell==[]:
        return result
    else: return [valor+dell[0]]+ comb_aux(valor,dell[1:])
print(combinaciones(hp,dell))
    
#####con cola
class combinacion():
    def __init__(self):
        pass
    def combinaciones2(self,hp,dell):
        if isinstance(hp,list) and isinstance(dell,list) and len(hp)>0 and len(dell)>0:
            return self.combinaciones2_aux(hp,dell,[])
        else: return "Error"

    def combinaciones2_aux(sefl,hp,dell,resultado):
        if hp==[]:
            return []
        else: return combinaciones_aux(hp[1:], dell, resultado +comb2_aux(hp[0],dell,[]))

    def comb2_aux(self,valor,dell,resultado):
        if dell==[]:
            return[]
        else:return comb2_aux(valor,dell[1:],resultado+[valor+dell[0]])
        
