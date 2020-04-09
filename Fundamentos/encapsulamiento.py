class Persona:
    def __init__(self, n, e):
        self.__nombre=n
        self.__edad=e
        
    def get_nombre(self):
        return self.__nombre
        
    def set_nombre(self, nombre):
        self.__nombre=nombre
        
    def get_edad(self):
        return self.__edad
    
    def set_edad(self, edad):
        self.__edad=edad
        
p1=Persona("Julian", 20)
#print(p1.__nombre) tira error6
print(p1.get_nombre())
print(p1.get_edad())

p1.set_nombre("Javier")
p1.set_edad("22")
print(p1.get_nombre())
print(p1.get_edad())
