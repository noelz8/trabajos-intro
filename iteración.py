def largo(Lista):
    Cont=0
    while Lista!=[]:
        Cont=Cont+1
        Lista=Lista[1:]

    return Cont


def cont_pares(Lista):
    Cont=0#Contador de pares
    for item in Lista:
        if item%2==0:
            Cont+=1
        #Lista=Lista[1:] For hace automático el slace de un objeto iterable
    return Cont

# Cantidad de dígitos que tiene un número
def digitos(Num):
    if isinstance(Num,int):
        if Num==0:
            return 1
        Dgts=0
        Num=abs(Num)

        while Num!=0:
            Num//=10
            Dgts+=1
        return Dgts#Note la sangria fuera de la raiz
    else:
        return "Error número debe ser entero"

def encont_par(Num):
    if not isinstance(Num,int):
        return "No Get Serius! Number must be an integer"

    if Num==0:
        return True

    Num=abs(Num)
    while Num!=0:
        if Num%2==0:
            return True
        Num=Num//10
        return False

    
