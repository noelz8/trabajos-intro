### matriz transpuerta, se ingresa una matriz que de una matriz como respuesta, usando clases,indices,recursion de cola

class Transpuesta(object):
    def __init__(self):
        pass

    def trans(self,matriz):
        if isinstance (matriz,list) and matriz !=[] :
            return self.trans_aux(matriz,0,0,[],[])
        else: return "Error"

    def trans_aux(self,matriz,f,cola,resultado,fila):
        if cola==len(matriz[0]):
            return resultado
        elif f==len(matriz):
            return self.trans_aux(matriz,[],cola+1,resultado+[fila],0)
        else: return self.trans_aux(matriz,f+[matriz[fila][cola],resultado,fila+[matriz[cola][f]]])
