#busqueda de un elemento en una matriz
class busqueda(object):
    def __init__(self):
        pass
    def busq(self,elemento,matriz):
        if isinstance (elemento,int) and isinstance (matriz,list):
            return self.busq_aux(elemento,matriz,0,0)
        else: return "error"

    def busq_aux(self,elemento,matriz,fila,columna):
        if fila==len(matriz):
            return False
        elif elemento==matriz[fila][columna]:
            return True
        elif columna==len(matriz[0])
        return self.busq_aux(matriz,fila+1,0,elemento)
    else: return self.busq_aux(matriz,fila,columna+1,elemento)
        
