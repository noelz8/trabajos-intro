import math
from FiguraInicial import Fig
class Cuadrado(Fig):
    def __init__self(x,y,lado):
        super().__init__(x, y)
        self.__lado= lado

    def getLado(self):
        return self.__lado
    def setLado(self,lado):
        self.__lado=lado

    def calcularArea(self):
        return self.__lado*self.__lado
