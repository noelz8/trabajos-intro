class rellenar(object):
    def __init__(self):
        pass
    def crear_matriz(self,n,m):
        if isinstance (n,int) and n>0 and isinstance (m,int) and m>0:
            return self.crear_matriz_aux(n,m,[],[],0,0)
        else: "Error"

    def crear_matriz_aux(self,n,m,matriz,fila,indicefila,indicecolumna):
        if indicefila==n:
            return matriz
        elif indicecolumna==m:
            return self.crear_matriz_aux(n,m,matriz+[fila],[],indicefila+1,0)
        elif indicefila==0 or indicefila==(n-1):
            return self.crear_matriz_aux(n,m,matriz,fila+["+"],indicefila,indicecolumna+1)
        elif indicecolumna ==0 or indicecolumna==(m-1):
            return self.crear_matriz_aux(n,m,matriz,fila+["*"],indicefila,indicecolumna+1)
        else: return self.crear_matriz_aux(n,m,matriz,fila+[0],indicefila,indicecolumna+1)
r=rellenar()
print(r.crear_matriz(4,5))
