class Persona:
    def __init__(self, nombre, apellido, edad):
        self.__nombre=nombre
        self.__apellido=apellido
        self.__edad=edad
        
    def __str__(self):
        return "Nombre: " + self.__nombre + "\nApellido: " + self.__apellido + "\nEdad: " + str(self.__edad)