import math
from FiguraInicial import Fig
class Circulo(Fig):
    def __init__(self,x,y,r):
        super().__init__(x,y)
        self.__radio=r
    def getRadio(self):
        return self._radio
    def setRadio(self,r):
        self.__radio=r
    def calcularArea(self):
        return math.pi*(self.__radio**2)



