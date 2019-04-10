#####Programar una clase que recibe una lsita desordenada y devuelve una ordenada. indices
class ordenar(object):
    def __init__(self):
        pass
    def orden(self,lista):
        if isinstance (lista,list) and lista !=[]:
            return self.orden_aux(lista,0)
        else: return "Error"

    def orden_aux(self,lista,indice):
        if indice==len(lista)-1:
            return lista
        else: return sefl.ordernar2_aux(lista,0)+orden_aux(lista,indice+1)

    def orden_aux2(self,lista,indice):
        if indice==len(lista)-1:
            return lista
        elif lista[inice]>lista[indice+1]:
            aux= lista[indice]
            lista[indice]=lista[indice+1]
            lista[indice+1]=aux
            return orden2_aux(lista,indice+1)
        else: return orden2_aux(lista,indice+1)
        
        
