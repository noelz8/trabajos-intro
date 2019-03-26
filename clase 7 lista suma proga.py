
#suma los valores de la lista
def suma(lista):
    #if type (lista) ==list
    if isinstance (lista, list):
        return suma_aux (lista)
    else: return "Error: el valor ingreado no es una lista"

def suma_aux(lista):
    if lista ==[]:
        return 0
    else:
        return lista[0] + suma_aux(lista[1:])
#La lista tiene que estar con el formato [] para que funcione NO con ()
def resta(lista):
    if (lista, list):
        return resta_aux(lista)
    else : return "Error: no es una lista"

def resta_aux(lista):
    if lista ==[]:
        return 0
    else:
        return lista[0] - resta_aux(lista[1:])

#Sumar todos los pares en una lista

def par_lista(lista):
    if isinstance (lista, list):
        return par_lista_aux(lista)
    else: return "Error"

def par_lista_aux(lista):
    if lista ==[]:
        return 0
    if (lista[0]%2==0):
        return lista[0]+par_lista_aux(lista[1:])
    else:
        return par_lista_aux(lista[1:])
    
def impar_lista(lista):
    if isinstance (lista, list):
        return impar_lista_aux(lista)
    else: return "Error"

def impar_lista_aux(lista):
    if lista ==[]:
        return 0
    if (lista[0]%2==1):
        return lista[0]+impar_lista_aux(lista[1:])
    else:
        return par_lista_aux(lista[1:])

#hace una funcion que indique si una lisra tiene al menos un cero.
    #la funcion debe regresar true o false.
def cero_lista(lista):
    if isinstance (lista, list):
        return cero_lista_aux(lista)
    else: return "Error"

def cero_lista_aux(lista):
    if lista ==[]:
        return False
    elif (lista[0]==0):
        return True
    else: return cero_lista_aux(lista[1:])
    
