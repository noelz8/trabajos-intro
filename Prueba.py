from Stock import Pila
class Pruebas:
    def __init__(self):
        self.__pila=Pila()

    def separar(self,num):
        while num>0:
            self.__pila.push(num%10)
            num=num//10
    def invertir(self):
        invertido=0
        potencia=0
        while not self.__pila.is_empty():
            invertido += self.__pila.pop()*10**potencia
            potencia +=1
        return invertido
    
    def ejecutar(self,num):
        self.separar(num)
        return self.invertir()
              
    
