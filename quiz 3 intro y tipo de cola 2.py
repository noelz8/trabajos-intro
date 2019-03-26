def par(num):
    cond=lambda digito: digito%2==0
    if isinstance (num,int):
        return par_aux(num,cond)
    else: return "Error"

def par_aux(num,cond):
    if num==0:
        return []
    elif cond(num%10):
        return[num%10]+par_aux(num//10,cond)
    else: return par_aux(num//10,cond)
#haceer que una funcion que multiplique los elementos de una lista por
#el resultado de multiplicaciones previas usando slicing

def multi(lista):
    if isinstance (lista,list) and lista !=[]:
        return multi_aux(lista,1)#si se quiere devolver lista en vez de 1 se pone []
    else: return "Error"

def multi_aux(lista,resultado):
    if lista==[]:
        return resultado###se regresa la funcion
    else:
        return multi_aux(lista[1:], resultado*lista[0])#despues de la coma es lo importante para la funcion
#hacer una funcion que reciba una lista y obtenga otra con lista con los pares

def par_lista(lista2):
    if isinstance (lista2,list) and lista2 !=[]:
        par= lambda numero: numero%2==0
        return par_lista_aux(lista2,[],par)
    else:
        return "Error"

def par_lista_aux(lista2,result,par):
    if lista2==[]:
        return result
    elif par(lista2[0]):
        return par_lista_aux(lista2[1:],result + [lista2[0]], par)
    else: return par_lista_aux(lista2[1:],result, par)
        
    
