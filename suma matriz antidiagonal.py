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

#### forma alterna

    def suma_antidiagonal(self,matriz):
        if isinstance (matriz,list) and matriz !=[] and len(matriz) ==len(matriz[0]):
            return self.antidiagonal_aux2(matriz,lne(matriz),0,0)
        else: return "Error"

    def antidiagonal_aux2(self,matriz,largo,fila,suma):
        if fila== largo:
            return suma
        else: return self.antidiagonal_aux2(matriz,largo,fila+1,suma+matriz[fila][-(fila+1)])

    
