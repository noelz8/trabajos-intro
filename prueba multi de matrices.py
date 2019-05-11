#Multiplicar matrices
class multi(object):
    def __init__(self):
        pass
    def multi_matriz(self,n,m):
        if isinstance (n,list) and n!=[] and isinstance (m,list) and m!=[]:
            return self.multi_aux(n,m,[],[],[],0,0)
        else: return "error"

    def multi_aux(self,n,m,resultado,matriz,fila,indicefila,indicecolumna):
        if indicefila==len(n):
            return matriz*resultado
        elif inidcecolumna==len(m[indicefila]):
            return self.multi_aux(n,m,resultado,matriz+[fila],[],indicefila+1,0)
        elif indicefila==0 or indicefila==(n-1):
            return self.multi_aux(n,m,resultado,matriz,fila,0,indicecolumna+1)
        else: return self.multi_aux(n,m,resultado,matriz,fila,indicefila,indicecolumna)
            
        
