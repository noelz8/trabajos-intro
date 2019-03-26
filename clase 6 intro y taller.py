#sacar numero apartir de pares de pares
#intento mio(revisar)
def pares2 (num,  potencia):
    if num ==0:
        return 0
    elif ((num%10)%2==0):
        return num//10*10**potencia+ pares(potencia+1)
    else:return pares2(num//10*10**potencia)
#respuesta profe
def forme_par(num):
    if isinstance (num, int):
        return forma_par_aux(num, 0)
    else: return "Error"

def forma_par_aux(num, potencia):
        if num==0: #rojo
             return 0
        elif num % 10 %2 == 0: #verde
            return (num //10)* (10**potencia)+ forma_par_aux(num//10, potencia+1)
        else: return forma_par_aux(num//10, potencia)
#Dado un numero, verifique que todos los digitos del numero se encuentra entre 0 y 4
        ####incorrecto
def entre(num):
    if isinstance (num,int) and num >0:
        return entre_aux(abs(num))
    else: return "Error"

def entre_aux(num):
    if (num==0):
        return True
    elif num%10 >=0 and num % 10<=4:
        return entre_aux(num//10)
    else: return False
#################Taller############################################
def sumatoria(n,i):
    if(i>n):
        return 0
    else: return (i + 3)+ sumatoria(n, i+1)

def sumatoria2(n):
    if(n<0):
        return 0
    else: return (n+3) + sumatoria2(n-1)
#secuencia de fibonacci

def secuencia(n,i):
    if(i>n):
        print( end=" ")
        return 1
    else: return (i- 1)+secuencia(n, i+1)
####respuesta profe
def fib(n):
    if isinstance (n,int):
        return fib_aux(n)
    else: return "Error"
def fib_aux(n):
    if n ==0:
        return 1
    elif n==1:
        return 1
    else:
        return fib_aux(n-1)+ fib_aux(n-2)
    #suma los valores de la lista
def suma(lista):
    #if type(lista)== list
    if isinstance (lista, list):
        return suma_aux
    else: return "Error: el valor ingressado no es una lista"

def suma_aux(lista):
    if lista ==[ ]:
        return 0
    else:
        return lista[0]+ suma_aux(lista[1:])#intervalo
    
