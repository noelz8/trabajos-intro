class buscar(object):
    def __ini__(self):
        pass
    def busqueda(self,num,lista):
        if isinstance (num,int) and isinstance (lista,list):
            return self.busqueda_aux(num,lista,0)
        else: return "Error"

    def busqueda_aux(self,num,lista,indice):
        if lista==[]:
            return -1
        elif lista[0]==num:
            return indice
        else: return self.busqueda_aux(num,lista[1:], indice+1)

    def busqueda2(self,num2,lista2):
        if isinstance (num,int) and isinstance (lista,list) and lista!=[]:
            return self.busqueda2_aux(num,lista,0,[])
        else: return "Error"

    def busqueda2_aux(self,num2,lista2,indice,result):
        if len(lista)==indice:
            return result
        elif lista[indice]==num:
            return busqueda2_aux(num,lista,indice+1, resultado+[indice])
        else : return self.busqueda2_aux(num,lista,indice+1,result)
#########se le conoce como busqueda lineal
