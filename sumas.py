def sumaWhile(lista):
    resultado=0
    contador=0
    largo=len(lista)
    while contador<largo:
        resultado+=lista[contador]
        contador+=1
    return resultado

def sumaSlicing(lista):
    resultado=0
    while lista !=[]:
        resultado+=lista[0]
        lista=lista[1:]
    return resultado

def sumaFor(lista):
    resultado=0
    for contador in range(len(lista)):
        resultado+=lista[contador]
    return resultado

def sumaFor(lista):
    resultado=0
    for valor in lista:
        resultado+=valor
    return resultado
    
