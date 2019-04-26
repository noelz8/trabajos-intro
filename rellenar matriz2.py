
#Rellenar una matriz opcion 2
class rellenar(object):
    def __init__(self):
        pass
    def crear_matriz(self,n):
        if isinstance (n,int) and n>0:
            return self.crear_matriz_aux(n,[],[],0,0)
        else: "Error"

    def crear_matriz_aux(self,n,matriz,fila,indicefila,indicecolumna):
        if indicefila==n:
            return matriz
        elif indicecolumna==n:
            return self.crear_matriz_aux(n,matriz+[fila],[],indicefila+1,0)
        elif indicefila==0 or indicefila==(n-1):
            return self.crear_matriz_aux(n,matriz,fila+["+"],indicefila,indicecolumna+1)
        elif indicecolumna ==0 or indicecolumna==(n-1):
            return self.crear_matriz_aux(n,matriz,fila+["*"],indicefila,indicecolumna+1)
        else: return self.crear_matriz_aux(n,matriz,fila+[0],indicefila,indicecolumna+1)
r=rellenar()
print(r.crear_matriz(5))


