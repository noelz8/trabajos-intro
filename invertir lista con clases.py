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
            #temp = lista[final]
            #lista[final]=lista[inicio]
            #lista[inicio]= temp
            return self.invertir_aux(lista,inicio+1,final-1)
#con solo 1 indice
    def invertir2(self,lista):
        if isinstance (lista,list) and lista !=[] and len(lista)%2==0:
            return self.invertir_aux(lista,0)
        else: return "Error"

    def invertir2_aux(self,lista,inicio):
        if inicio==len(lista)//2:
            return lista
        else:
            lista[-(inicio+1)],lista[incio]=lista[inicio],lista[-(inicio+1)]
            return self.invertir_aux(lista,inicio+1)
     
