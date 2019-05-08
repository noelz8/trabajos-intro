"""
Ejercicio 7b
Hansel Hampton Fallas
08/05/2019
"""
class Vehiculo:
    def __init__(self, placa, marca, ruedas, consumo):
        self.placa=placa
        self.marca=marca
        self.ruedas=ruedas
        self.km=0
        self.combust=0
        self.consumo=consumo
    def mostrar(self):
        print("# de placa: ", self.placa, "\nMarca: ", self.marca, "\nKilometraje: ", self.km, "\nCombustible restante: ", self.combust, "\nConsumo: ", self.consumo)
    def hacerViaje(self, kms):
        self.km+=kms
        print("Kilometraje actualizado")
    def set_combustible(self, x):
        self.combust=x
        print("Combustible asignado")
    def reset_km(self):
        self.km=0
        print("Kilometraje restaurado")
    def get_variables(self):
        print("Kilometraje actual: ", self.km, "\nCombustible actual: ", self.combust)
        return self.km, self.combust
class Auto(Vehiculo):
    def __init__(self, placa, marca, ruedas, consumo, modelo, año):
        Vehiculo.__init__(self, placa, marca, ruedas, consumo)
        self.model=modelo
        self.año=año
    def mostrar(self):
        print("# de placa: ", self.placa, "\nMarca: ", self.marca, "\nModelo: ", self.model, "\nAño: ", self.año, "\nKilometraje: ", self.km, "\nCombustible restante: ", self.combust, "\nConsumo: ", self.consumo)
class Moto(Vehiculo):
    def __init__(self, placa, marca, ruedas, consumo, estilo, cilindraje):
        Vehiculo.__init__(self, placa, marca, ruedas, consumo)
        self.estilo=estilo
        self.cilind=cilindraje
    def mostrar(self):
        print("# de placa: ", self.placa, "\nMarca: ", self.marca, "\nEstilo: ", self.estilo, "\nCilindraje: ", self.cilind, "\nKilometraje: ", self.km, "\nCombustible restante: ", self.combust, "\nConsumo: ", self.consumo)
global McQueens
McQueens=[Auto("GHHJ33", "TOYOTA", 4, 17, "VITARA", "2010"), Auto("CM4253", "CAMEL", 4, 8, "DROMEDARIO", "54"), Moto("GDHT57", "YAMAHA", 2, 7, "MONTAÑERA", "125"), Auto("VJHB45", "AUDI", 4, 20, "E-TRON GT", "2019"), Moto("RG2352", "SUSUKI", 2, 5, "PISTERA", "250"), Moto("RT4353", "HONDA", 2, 10, "MONTAÑERA", "175")]
def revise(lista):
    rslt=[]
    for i in range(len(lista)):
        if lista[i].km > 10000:
            rslt.append(lista[i])
    if rslt==[]:
        print("De momento, ningún vehículo supera los 10.000 Km")
    else:
        print("Vehículos con más de 10.000 Km:\n")
        for i in range(len(rslt)):
            rslt[i].mostrar()
            print("\n")
