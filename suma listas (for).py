#Sume los valores de 2 listas de igual tamaño usando un for e indices.El resultado es nùmero con la suma de ambas
class suma(object):
    def __init__(self):
        pass
    def sumar(self,lista,lista2):
        sumar=0
        if len(lista)==len(lista2):
            largo=len(lista)
            for indice in range(largo):
                sumar+=lista[indice]+lista2[indice]
            return sumar
        else: "Error"

    def sumar_lista(self,lista,lista2):
        sumar_lista=[]
        if len(lista)==len(lista2):
            largo=len(lista)
            for indice in range(largo):
                sumar_lista+=[lista[indice]+lista2[indice]]
            return sumar_lista
        else: "Error"
#Sumar matriz
    #def sumar_matriz(self,matriz,matriz2):
        #filas=len(matriz)
        #columnas=len(matriz[0])
       # if fila==len(matriz2) and columnas==len(matriz2[0]):
      #      return self.sumar_matriz_aux(matriz,matriz2,filas,columnas)
     #   else:return "error"
    #def sumar_matriz_aux(self,matriz,matriz2,filas,columnas):
        #matriz3=[]
        #for fila in range(filas):
         #   for matriz3
    
    def recorrer(self):
        lista=[5,2,37,8,89]
        suma=0
        for valor in lista:
            suma+=valor
        print(suma)
        suma=0
        for indice in range(len(lista)):
            suma+=lista[indice]
        print (suma)
        suma=0
        contador=0
        while contador<len(lista):
            suma+=lista[contador]
            contador+=1

        print (suma)
