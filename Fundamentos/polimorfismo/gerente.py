from empleado import Empleado

class Gerente(Empleado):
    def __init__(self, nombre, sueldo, depto):
        super().__init__(nombre, sueldo)
        self.depto=depto
        
    def __str__(self):
        return super().__str__() + "\nDepartamento: " + self.depto