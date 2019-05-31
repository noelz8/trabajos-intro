#Rellenar matriz con for
class relleno(object):
    def __init__(self):
        pass
    def rellenar(self,alto,ancho):
        for fila in range(alto):
            for columna in range(ancho):
                if  fila==0 or fila==(alto-1):
                    print("*",end=" ")
                elif columna==0 or columna==(ancho-1):
                    print("*", end=" ")
                else: print(" ", end=" ")
            print("")
#Triangulo seria ((num*2)-1)//2

    def traingulo(self,base):
        filas=(base*2)-1
