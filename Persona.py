class Persona:
    def __init__(self,nombre,cedula.edad):
        self.__nombre=nombre
        self.__cedula=cedula
        self.__edad=edad
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,nombre):
        if isinstance (nombre,str):
            self.__nombre=nombre
        else: print( "El nombre no esun string")
    @property
    def cedula(self):
        return self.__cedula
    @cedula.setter
    def cedula(self,cedula):
        if isinstance (cedula,int):
            self.__cedula=cedula
        else: print("la cedula no esun numero")
    @property
    def edad(self):
        return self.__edad
    @edad.setter
    def edad(self):
        return self._edad
    @edad.setter
    def edad(self,edad):
        if isinstance (edad,int):
            self.__edad=edad
        else: print("valor no es numero")
    
