def lista_sumatoria(L1):
    if isinstance (L1,list):
        return sumatoria_aux(L1, len(L1))
    else: "Error"

def sumatoria_aux(lista,n):
    #condicon de parada
    if(n==0):
        return 0
    else:
        return (lista[n-1] * n-1*5**3)+ sumatoria_aux(lista, n-1)

def lista_sumatoria2(L1):
    if isinstance (L1,list):
        return sumatoria2_aux(L1, len(L1))
    else: "Error"


def sumatoria2_aux(lista,n):
    #condicon de parada
    if(lista==[]):
        return 0
    else:
        return (lista[-1] * (len(lista)-1)*5**3)+ sumatoria2_aux(lista [:-1])
