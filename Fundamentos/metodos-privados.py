class Persona:
    def __init__(self, nombre, nombre2, ape_paterno, ape_materno):
        self.nombre=nombre
        self.__segundo_nombre=nombre2
        self._apellido_paterno=ape_paterno
        self.__apellido_materno=ape_materno
        
    def metodo_publico(self):
        self.__metodo_privado()
        
    def __metodo_privado(self):
        print(self.nombre)
        print(self.__segundo_nombre)
        print(self._apellido_paterno)
        print(self.__apellido_materno)
        
    def get_apellido_materno(self):
        return self.__apellido_materno
    
    def set_apellido_materno(self, ape_materno):
        self.__apellido_materno=ape_materno
        
    def get_segundo_nombre(self):
        return self.__segundo_nombre
    
    def set_segundo_nombre(self, nombre2):
        self.__segundo_nombre=nombre2
    
p1=Persona("Julian", "Nicolas", "Schmidt", "Cipollari ")
p1.metodo_publico()

print(p1.nombre)
print(p1.get_segundo_nombre())
print(p1._apellido_paterno)
print(p1.get_apellido_materno())