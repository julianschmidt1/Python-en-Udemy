class Persona:
    def __init__(self, nombre):
        self.__nombre=nombre
    
    #Metodo sobreescrito de object
    def __add__(self, otro):
        return self.__nombre + " y " + otro.__nombre
        
p1=Persona("Julian")
p2=Persona("Sofia")

print(p1+p2)