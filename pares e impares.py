#Dado un numero, almacenar los digitos pares de este en una lista y los digitos impares en otra lista.Use while
class separar(object):
    def __init__(self):
        pass
    def listas(self,num):
        if isinstance (num,int) and num>=0:
            return self.listas_aux(num)
    def listas_aux(self,num):
        listaPares=[]
        listaImpares=[]
        while num>0:
            digi=num%10
            if (digi%2==0):
                listaPares +=[digi]
            else: listaImpares+=[digi]
            num=num//10
        return listaPares,listaImpares
