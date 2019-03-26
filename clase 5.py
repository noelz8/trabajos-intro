def regresivo(i):
    print (i, end=" ")
    if(i <=1):
        return
    else: regresivo(i-1)



def cuenta(w):
    print(w)
    cuenta(w-1)



def fact(x): #sacar factor de un numero, osea multiplica por el numero anterior
    if x ==0:
        return 1
    else:return x * fact(x-1)


def prueba(a):
    print (a, end=" ")
    if (a<=1):
        return
    else: prueba(a//10)
    

def suma_digitos(num):
    if (num==0): #rojo
        return 0
    else: #verde
        return num % 10+ suma_digitos(num//10)
#entrada: es un numero entero
    #restricciones: es un entero positivo mayor a cero
    #sañida: suma de los digitos
def longitud_numeros(num):#saber cuantos digitos tiene el numero
    if isinstance (num, int) and (num >0):
        return longitud_numerosaux(abs(num))
    else:
        return "Error"
            
def longitud_numeros_aux(num):
    if (num==0):
        return 0
    else:
        return 1+ suma_digitos_aux(num //10)

    
#determinar cuantas veces aparece un digito en un numero
    #entrada: es un numero entero
    #restricciones
    #salida: longitud de un numero
        #encontrar (num, dig)
    
def longitud_numeros2(num, dig):
    if (isinstance (num, int) and (num >=0) and (num >0)) and (isinstance(dig, int) and dig>=0) :
        
        return longitud_numeros_aux2(num, dig)
    else:
        return "Error"
    
def longitud_numeros_aux2(num, dig):
        if (num==0): #rojo
             return 0
        elif (num % 10 == dig): #verde
            return 1+ longitud_numeros_aux2(num //10, dig)
        else: return longitud_numeros_aux2(num//10, dig)
        
                
#determinar cuantos numeros pares aparecen en un numero
        
def prueba(num):
    if (isinstance (num, int) and (num >=0) and (num >0)):
        
        return prueba_aux(num)
    else:
        return "Error"
    
def prueba_aux(num):
        if (num==0): #rojo
             return 0
        elif ((num % 10) %2 == 0): #verde
            return 1+prueba(num //10)
        else: return prueba(num//10)
#Saber cuantos digitos pares o impares hay en el numero(probar para la tarea :v)
def pares_impares (num):
    if isinstance (num, int) and num >0:
        return pares (num), impares (num)
    else: return "Error"
    ###########################################
def pares (num):
    if num ==0:
        return 0
    elif((num%10)%2==0):
        return 1+ pares(num//10)
    else:return pares(num//10)

def impares (num):
    if num==0:
        return 0
    elif num %10 %2==1:
        return 1 + impares(num//10)
    else:
        return impares (num // 10)
    
    

