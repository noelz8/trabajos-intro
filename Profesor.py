from Persona import Persona
class Profesor(Persona):
    def __init__(self,nombre.cedula,edad,escuela,cursos):
        super().__init__(nombre,cedula,edad)
        self.__escuela=escuela
        self.__cursos=cursos
    @property
    def escuela(self):
        return self.__escuela
    @escuela.setter
    def escuela(self,escuela):
        self.__escuela=escuela
    @property
    def cursos(self):
        return self.__cursos
    @cursos.setter
    def cursos(self,cursos):
        self.__cursos=cursos
