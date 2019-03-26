class Operaciones:
    def __init__(self):
        pass
    def largo(self,num):
        if isinstance(num, int):
            return self.largo_aux(num, 0)
        else:
            return "Error"
        def largo_aux(self, num, resultado):
            print(resultado)
            if(num==0):
                return resultado
            else:
                return self.largo_aux(num//10, resultado +1)
    
#hacer una funcion que reciba un numero entero
#que elimine los digitos que son divisibles en 3
def potencia(num):
    if isinstance (num, int):
        return potencia_aux(num, 0,0)
    else:
        return "Error"
def potencia_aux(num, result, exp):
    if num==0:
        return result
    elif (num%10)%3==0 and (num%10) !=0:
        return potencia_aux(num//10,result, exp)
    else: return potencia_aux(num//10, result + num%10*10**exp, exp+1)
