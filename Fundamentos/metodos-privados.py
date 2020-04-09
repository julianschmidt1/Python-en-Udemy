class Persona:
    def __init__(self, nombre, ape_paterno, ape_materno):
        self.nombre=nombre
        self._apellido_paterno=ape_paterno
        self.__apellido_materno=ape_materno
        
    def metodo_publico(self):
        self.__metodo_privado()
        
    def __metodo_privado(self):
        print(self.nombre)
        print(self._apellido_paterno)
        print(self.__apellido_materno)
        
    def get_apellido_materno(self):
        return self.__apellido_materno
    
    def set_apellido_materno(self, ape_materno):
        self.__apellido_materno=ape_materno
    
p1=Persona("Julian", "Schmidt", "Cipollari ")
p1.metodo_publico()

print(p1.nombre)
print(p1._apellido_paterno)
print(p1.get_apellido_materno())