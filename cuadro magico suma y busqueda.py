class magico(object):
    def __init__(self):
        pass
    
    def conse(self,matriz):
        if isinstance (matriz,list) and len(matriz)==len(matriz[0]):
            return self.conse_aux(matriz,1)
        else: return "Error"

    def conse_aux(self,matriz,contador):
        if contador >(len(matriz)*len(matriz[0])):
            return True
        elif self.buscar(contador,matriz,0,0):
            return self.conse_aux(matriz,contador+1)
        else: return False

    def buscar(self,elemento,matriz,fila,columna):
        if fila==len(matriz):
            return False
        elif columna==len(matriz[0]):
            return self.buscar(elemento,matriz,fila+1,0)
        elif elemento==matriz[fila][columna]:
            return True
        else: return self.buscar(elemento,matriz,fila,columna+1)

c = magico()
print (c.conse([[3,2],[1,4]]))
