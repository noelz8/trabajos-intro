#hacer una suma de matriz antidiagonal
class Matriz(object):
    def __init__(self):
        pass
    def antidiagonal (self,matriz):
        if isinstance (matriz,list) and len(matriz[0])==len(matriz) and matriz !=[]:
            return self.antidiagonal_aux(matriz,0,0,len(matriz)-1)
        else: return "Error"

    def antidiagonal_aux(self,matriz,resultado,fila,col):
        if fila==len(matriz):
            return resultado
        else: return self.antidiagonal_aux(matriz,resultado+matriz[fila][col],fila+1,col-1)

    
