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
        else: return self.orden_aux(sefl.orden_aux2(lista,0),indice+1)

    def orden_aux2(self,lista,indice):
        if indice==len(lista)-1:
            return lista
        elif lista[inice]>lista[indice+1]:
            aux= lista[indice]
            lista[indice]=lista[indice+1]
            lista[indice+1]=aux
            return self.orden_aux2(lista,indice+1)
        else: return self.orden_aux2(lista,indice+1)
        
    ### se usa el ordenamiento burbuja
        #alternativo
        def orden2(self,lista):
        if isinstance (lista,list) and lista !=[]:
            return self.orden2_aux(lista,0,0)
        else: return "Error"

    def orden2_aux(self,lista,indice1,indice2):
        if indice2==len(lista)-1:
            return lista
        elif indice1==len(lista)-1:
            return orden2_aux(lista,0,indice2+1)
        elif
        
