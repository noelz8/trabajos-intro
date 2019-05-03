class Inv(object):
    def __init__(self):
        pass
    def invertir(self,lista):
        if isinstance (lista,list) and lista !=[] and len(lista)%2==0:
            return self.invertir_aux(lista,0,len(lista)-1)
        else: return "Error"

    def invertir_aux(self,lista,inicio,final):
        if inicio>final:
            return lista
        else:
            lista[inicio],lista[final]=lista[final],lista[inicio]
            return self.invertir_aux(lista,inicio+1,final-1)
     
