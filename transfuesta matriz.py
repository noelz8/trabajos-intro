#Trasponer una matriz
class matrices(object):
    def __init__(self):
        pass
    def transpuesta(self,matriz):
        if isinstance (matriz,list):
            filas=len(matriz)
            columnas=len(matriz[0])
            return self.transpuesta_aux(matriz,filas,columnas)
        else: "Error"

    def transpuesta_aux(self,matriz,fila,columnas):
        transpuesta=[]
        for columna in range(columnas):
            filaTranspuesta=[]
            for fila in range(filas):
                filaTranspuesta+=[matriz[fila][columna]]
            transpuesta+=[filaTranspuesta]
        return transpuesta
#suma de diagonal
    def diagonal(self,matriz):
        if isinstance (matriz,list):
            filas=len(matriz)
            return self.diagonal_aux(matriz,filas)
        else: "Error"

    def diagonal_aux(self,matriz,filas):
        diagonal=0
        for fila in range(filas):
            diagonal+=[matriz[fila][fila]]
        return diagonal
    
    def antidiagonal(self,matriz):
        if isinstance (matriz,list):
            filas=len(matriz)
            return self.diagonal_aux(matriz,filas)
        else: "Error"

    def antidiagonal_aux(self,matriz,filas):
        antidiagonal=0
        for fila in range(filas):
            diagonal+=[matriz[fila][fila][-(fila+1)]]
        return antidiagonal
        
