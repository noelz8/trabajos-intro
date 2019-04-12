###suma de 2 matrices
class matrices(object):
    def __init__(self):
        pass
    def matriz(self,matr1,matr2):
        if isinstance (matr1,list) and isinstance (matr2,list) and len(matr1[0])==len(matr2[0]):
            return self.matriz_aux(matr1,matr2,0,0,[],[])
        else: return "Error"

    def matriz_aux(self,matr1,matr2,f,c,resultado,fila):
        if f==len(matr1):
            return resultado
        elif c==len(matr1[0]):
            return self.matriz_aux(matr1,matr2,f+1,0,resultado+[fila],[]) 
        else: return self.matriz_aux(matr1,matr2,f,c+1, resultado,fila+[matr1[f][c]+matr2[f][c]])

 
