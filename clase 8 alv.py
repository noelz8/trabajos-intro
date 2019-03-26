#lista verificacion positivo
def listap(lista):
    if isinstance (lista, list) and lista != []:
        return listap_aux(lista)
    else: return "Error"

def listap_aux(lista):
    if lista ==[]:
        return True
    elif (lista[0] < 0):
        return False
    else: return listap_aux(lista[1:])
######Lista y un numero, elimine ese numero de la lista.
def funcion(lista, num):
    if isinstance(lista, list):
        return funcion_aux(lista, num)
    elif isinstance (n, list):
        return funcion_aux(lista, num)
    else: return "Error"

def funcion_aux(lista, num):
    if lista==[]:
        return []
    elif lista[0]==n:
        return funcion_aux(1[1:],n);
    else:
        return lista[0]+funcion(lista[1:], num)
#Respuest profe
def eliminar (lista, elemento):
    if ((isinstance (lista, list) and lista != [] and isinstance (elemento, int)) and elemento >=0):
        return eliminar_aux(lista, elemento)
    else: return " Revise parametros"

def eliminar_aux(lista, elemento):
    if lista == []:
        return []
    elif lista [0] == elemento:
        return eliminar_aux(lista[1:], elemento)
    else: return [lista[0]] + eliminar_aux(lista[1:], elemento)
 ################################################################   
#Determinar el minimo de una lista
def lista_minimo(lista):
    if isinstance (lista, list):
        return lista_minimo_aux(lista)
    else: return "Error no hay minimo"

def lista_minimo_aux(lista):
    if lista ==[]:
        return 0
    elif lista[0]== lista[0:]:
        return min
    else: return [lista[0]] - lista_minimo_aux(lista[0:])
### respuesta profe########################################
def minux(lista):####analizar########!!!!!!
    if isinstance (lista, list):
        return minimum(lista)
    else: return "Error"
    
def minimum(lista):
    if lista [1:]== []: # rojo
        return lista[0]
    elif lista [0] <= lista [1]: #verde
        return minimum([lista[0]] + lista[2:])
    else: return minimum (lista[1:])
##########################################################
#sacar el valor mayor

def mayor(lista):
    if isinstance (lista, list):
        return maximum(lista)
    else: return "Error"

def maximum(lista):
    if lista[1:]== []:
        return lista [0]
    elif lista[0]>= lista[1]:
        return maximum([lista[0]]+ lista[2:])
    else: return maximum(lista[1:])
