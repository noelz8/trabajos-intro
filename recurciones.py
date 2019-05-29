#Recursion de pila
class uso_fila(object):
    def __init__(self):
        pass
    
    def simple_pila(num,n):
        if isinstance (num,int) and isinstance (n,int):
            return self.simple_pila_aux(num,n -1)
    def simple_pila_aux(self,num,n):
        if n==0:
            return 0
        else: return (num*n)+self.simple_pila_aux(num,n-1)
#Recursion de cola
    def simple_cola(self,num,n):
        if isinstance (num,int) and isinstance (n,int):
            return self.simple_cola_aux(num,n-1,0)
    def simple_cola_aux(self,num,n,resultado):
        if n==0:
            return resultado
        else: return self.simple_cola_aux(num,n-1,resultado+num*n)
        
    def simple_iteracionWhile_aux(self,num,n):
        resultado=0
        while n>0:
            resultado +=(num*n)
            n-=1
    def simple_iteracionFor_aux(self,num,n):
        resultado=0
        for i in range(n):
            resultado+=(num*(i+1))
            print (num*(i+1))
