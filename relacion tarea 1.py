# -*- coding: latin-1 -*-

def centigrados_farenheit(centigrados):
        if(type(centigrados) == int or type(centigrados) == float):
                return calcular(centigrados)
        elif(type(centigrados) == str):
                cent = float(centigrados)
                calc = calcular(cent)
                print("print: " + str(calc))
                return calc
        else: return "Error"

def farenheit_centigrados(far):
        cent = (far - 32) / 1.8
        print("La conversion de grados Farenheit a centigrados es de " + str(cent))

def calcular(centigrados):
        return 9 / 5 * centigrados + 32

def binario(a):
        print (a,end=" ")
        if(a ==1):
                return
        else:binario (a//2)
        
        

def prueba(a):
        print("numero")
        base= input()
        print(a,end=" ")
        if (a==1):
                return
        else:base (a//input())
       
def binario2(a):
        print (a,end=" ")
        cantidad = int(input("Dígame una base: "))
print(f"{cantidad} base es {round(a // base)} ")
        
        if(a==1):
                return
        else:binario2 (a//b)
          
        

        
         
        

