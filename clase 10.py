def revise_num(num):
    if isinstance (num, int):
        entre0y4= lambda digito : digito <= 4
        entre5y9= lambda digito: digito >=5
        return revise_aux(num, entre0y4), revise_aux(num, entre5y9)
    else: return "Error"

def revise_aux(num, condicion):
    if num ==0:
        return 0
    elif condicion(num%10):
        return 1+ revise_aux(num //10, condicion)
    else: return revise_aux(num//10, condicion)

#####Hacer una funcion que recibe como parametro una lista de numeros positivos y negativos
##y los clasifica enlistas diferentes. La funcion regresa una tupla con 2 elementos: la listta de
#numeros positivos y la lista de negativos
#saca 2 listas 
def revise_pom(L1):
    if isinstance (L1, list) :
        positivo = lambda numero: numero >=0
        negativo = lambda numero: numero <=0
        return revise_pom_aux(L1, positivo), revise_pom_aux(L1, negativo)
    else: return "Error"

def revise_pom_aux(L1, condicion):
    if (L1 ==[]):
        return []
    elif condicion(L1[0]):
        return  [L1[0]] + revise_pom_aux(L1[1:], condicion)
    else: return revise_pom_aux(L1[1:], condicion)
###############opcion alterna
def probarpositivo(num):
    if num >0:
        return True
    else: return False

def revise_pom_aux(L1, condicion):
    if (L1 ==[]):
        return []
    elif probarpositivo(L1[0]):
        return  [L1[0]] + revise_pom_aux(L1[1:], condicion)
    else: return revise_pom_aux(L1[1:], condicion)
##############
######Hcaer una funcion que recibe como parametro una lsita de numeros, y los clasifica en listas
# de numeros, y los clasifica en listas diferentes en funcion de si son pares o impares

def revise_par(L1):
    if isinstance (L1, list) :
        par = lambda numero: numero%2 ==0
        impar = lambda numero: numero%2 == 1
        return revise_par_aux(L1, par), revise_par_aux(L1, impar)

def revise_par_aux(L1, condicion):
    if(L1==[]):
        return []
    elif condicion(L1[0]):
        return [L1[0]] + revise_par(L1[1:], condicion)
    else: return revise_par_aux(L1[1:], condicion)
                



                  
                  
    
