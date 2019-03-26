def suma_lista(lista1, lista2):
    if isinstance (lista1, list) and isinstance (lista2, list) and len(lista1) == len(lista2):
        return suma_lista_aux(lista1, lista2)
    else: return "Error"

def suma_lista_aux(lista1, lista2):
    if lista1 == [] and lista2 == []:
        return []
    else:
        return [lista1[0]+lista2[0]] + suma_lista_aux(lista1[1:], lista2[1:])

##########RESPUESTA###################################
##Suma binaria
def suma_bin(lista1,lista2,acarreo):
    if isinstance(lista1,list) and isinstance (lista2, list) and (acarreo, int ) and len(lista1)==len(lista2) and isinstance (acarreo,int):
        return suma_bin_aux(lista1,lista2,acarreo)
    else: return "error"

def suma_bin_aux(lista1,lista2,acarreo):
    if lista1==[] and lista2==[] and acarreo>0:
        return [acarreo]
    elif (lista1[-1]+lista2[-1]+acarreo)==2:
        return (suma_bin_aux(lista1[:-1], lista2[:-1], 1))+[0]
    elif (lista1[-1]+lista2[-1]+acarreo)==3:
        return (suma_bin_aux(lista1[:-1], lista2[:-1], 1)+[1]
