class promedio(object):
    def __init__(self):
        pass
    def promedio(self,matriz):
        if isinstance (matriz,list) and matriz !=[]:
            return self.promedio_aux(matriz,0,0,0)
        else: return "Error"

    def promedio_aux(self,matriz,filas,columnas,resultado):
        if filas==len(matriz):
            return resultado//len(matriz)*len(matriz[0])
        elif columnas==len(matriz[0]):
            return self.promedio_aux(matriz,filas+1,0,resultado)
        else: return self.promedio_aux(matriz,filas,columnas+1,resultado+matriz[filas][columnas])

#sacar promedio de matriz con slicecing
class promedio2(object):
    def __init__(self):
        pass

    def promedio_s(self,matriz2):
        if isinstance (matriz2,list) :
            return self.promedio_s_aux(matriz2,0)//len(matriz2)*len(matriz2[0])
        else: return "Error"

    def promedio_s_aux(self,matriz2,resultado):
        if matriz2==[]:
            return resultado
        elif (isinstance (matriz2[0],list)):
            return self.promedio_s_aux(matriz2[0],resultado) +self.promedio_s_aux(matriz2[1:],resultado)
        else: return self.promedio_s_aux(matriz2[1:],resultado+matriz2[0])
