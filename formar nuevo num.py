#Dado un numero,forme un nuevo numero solo con los digitos pares
class nuevo(object):
    def __init__(self):
        pass
    def par(self,num):
        if isinstance (num, int):
            return self.par_aux(num, 0)

    def par_aux(self,num, potencia):
        resultado=0#define lo que se va devolver
        while num>0:#condicion que se debe cumplir
            digi=num%10
            if (digi%2==0):
                resultado+=digi* (10**potencia)
                potencia+=1
                num//=10
                return resultado

        def par(self,num):
        if isinstance (num, int):
            return self.par_aux(num, 0)

    def par_aux(self,num, potencia):
        resultado=0#define lo que se va devolver
        impar=0
        
        while num>0:#condicion que se debe cumplir
            digi=num%10
            if (digi%2==0):
                resultado+=digi* (10**potencia)
                potencia+=1
                num//=10
                return resultado
    
    
