import math
from cuadrado import Cuadrado
class Rectangulo(Cuadrado):
    def __init__(self,x,y,lado,ancho):
        super().__init__(x,y,lado)
        self.ancho=ancho

    def getAncho(self):
        return self.__ancho
    def setAncho(self,ancho):
        self.__ancho=ancho

    def calcularArea(self):
        return super().getLado()*self.__ancho
