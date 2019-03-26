def division(divisor):
    if isinstance (divisor, int):
        if divisor==0 or divisor==1:
            return []
        else:
            return division_aux(divisor,2)
    else: return "Error"

def division_aux(divisor,contador):
    if contador==divisor:
        return []
    elif divisor%contador==0:
        return [contador]+division_aux(divisor, contador+1)
    else:
        return division_aux(divisor,contador+1)

########################suma lista con sub listas y sin listas
def sumar(lista):
    if isinstance (lista[0],list):
        return sumar_sub_aux(lista)
    else: return "Error"

def sumar_sub_aux(lista):
    if lista==[]:
        return 0
    if isinstance (lista[0],list):
        return sumar_sub_aux(lista[0]+lista[1:])
    #return sumar_lista(lista[0])+sumar_lista(lista[1:])
    else: return lista[0]+ sumar_sub_aux(lista[1:])
#
def param(digi,num):
    if isinstance (digi,int) and (num,int):
        return param_aux(num,digi,0)
    else: return "Error"

def param_aux(digi,num,n):
    if num==0:
        return 0
    elif digi*(num//10)<9:
        return param_aux(digi,num//10n)
    else: return param_aux(digi*(num//10)**n)+param_aux(dig,(num//1
