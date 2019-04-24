#dadad una matriz n x n, sumar los valores de su diagonal. Utilice recursion de cola e indices. crear una clase y la funcion de validacion
class Matrices (object):
    def __init__(self):
        pass
    def diagonal(self,matriz):
        if isinstance (matriz,list) and len(matriz[0])==len(matriz) and matriz !=[]:
            return self.diagonal_aux(matriz,0,0)
        else: return "error"
    def diagonal_aux(self,matriz,resultado,indice):
        if indice==len(matriz):
            return resultado
        else: return self.diagonal_aux(matriz,resultado+matriz[indice][indice],indice+1)
        
