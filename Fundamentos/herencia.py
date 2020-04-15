class Persona:
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad
    
    def __str__(self):
        return "Nombre: " + self.nombre + "\nEdad: " + str(self.edad)
    
class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo=sueldo
        
    def __str__(self):
        return super().__str__() + "\nSueldo: " + str(self.sueldo)
        
persona=Persona("Julian", 20)
print(persona)

empleado=Empleado("Marcos", 27, 50000)
print(empleado)

empleado.nombre="Jorge"
empleado.edad=25
empleado.sueldo=25000
print(empleado)