import math
def crecimiento(lista):
    if isinstance (lista,list) and len(lista):
        return crecimiento_aux(lista)
    else: "Error"

def crecimiento_aux(lista):
    if lista==[]:
        return []
    else:
        return [(lista[0]*crecimiento_aux(lista[:-1])),(math.sqrt(lista[0]+crecimiento_aux(lista[1:])))]
########## opcion 2############3
    #import math
#def crecimiento(lista):
 #   if isinstance (lista,list) and len(lista):
  #      return crecimiento_aux(lista,0,0)
   # else: "Error"

#def crecimiento_aux(lista, completo,medio):
 #   if lista==[]:
  #      return []
   # else:
    #    return crecimiento_aux(lista[0]*lista[:-1], math.sqrt(completo), medio-1)
    #####
    #####NOTA: me esta dando un error que dice una linea repite y a veces no pasa el error
