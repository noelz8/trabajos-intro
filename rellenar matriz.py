#rellenar una matriz con asteristicos
class asteristico(object):
    def __init__(self):
        pass
    def ast(self,matriz):
        if isinstance (matriz,list):
            return self.ast_aux(matriz,0,0)
        else: return "Error"

    def ast_aux(self,matriz,fila,columna):
        if fila==len(matriz):
            return matriz
        elif columna==len(matriz[0]):
            return self.ast_aux(matriz,fila+1,0)
        elif fila==0 or fila ==(len(matriz)-1) or columna==0 or columna==(len(matriz[0])-1):
            
            matriz[fila][columna]="*"
            return self.ast_aux(matriz,fila,columna+1)
        else: return self.ast_aux(matriz,fila,columna+1)
       

m= asteristico()
matriz= [[0,0,0,0],[0,0,0,0],[0,0,0,0]]
print(m.ast(matriz))
