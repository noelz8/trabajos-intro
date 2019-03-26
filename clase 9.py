###############SUMAR RAIZ CUADRada de los valores de una lista
import math
def suma_raiz(L1):
    if isinstance (L1, list):
        return suma_raiz_aux(L1)
    else: "error"

def suma_raiz_aux(L1):
    if (L1==[]):
        return 0
    else:
        return ( math.sqrt(L1[0]) + suma_raiz_aux(L1[1:]))
            
