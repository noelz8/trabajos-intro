###crear una clase que una matriz suma sus elementos, usando cola e indices
class suma(object):
    def __init__(self):
        pass
    def suma_matriz(self,matr):
        if isinstance (matr,list) and matr!=[]:
            return self.suma_aux(matr,0,0,0)
        else: return "Error"

    def suma_aux(self,matr,indice,indice2,result):
        if indice==len(matr):
            return result
        elif indice2==len(matr[indice]):
            return self.suma_aux(matr,indice+1,0,result)
        else: return self.suma_aux(matr,indice,indice2+1,result)+matr([indice][indice2])
#### respuesta alt

    def suma_matriz2(self,matriz):
        if isinstance (matr iz,list) and matriz !=[]:
            return self.matriz_aux(matriz,0,0)
        else: return "Error"

    def matriz_aux(matriz,fila,resultado):
        if fila=len(matriz):
            return resultado
        elif (isinstance(matriz[fila],list)):
            return self.fila_aux(matriz[fila],0,resultado)+matriz_aux(matriz,fila+1,resultado)
        else: return (matriz,fila+1,resultado)

    def fila_aux(matriz,col,resultado):
        if(col==len(fila)):
            return resultado
        else: return self.fila_aux(fila,col,resultado+fila[col])
                                   
