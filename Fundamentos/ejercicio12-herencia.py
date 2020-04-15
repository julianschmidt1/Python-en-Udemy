class Vehiculo:
    def __init__(self, color, ruedas):
        self.color=color
        self.ruedas=ruedas
        
    def __str__(self):
        return "Color: " + self.color + "\nRuedas: " +str(self.ruedas)
    
class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad=velocidad
        
    def __str__(self):
        return super().__str__() + "\nVelocidad: " +str(self.velocidad)+"km/h"
    
class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo=tipo
        
    def __str__(self):
        return super().__str__()+"\nTipo: "+self.tipo
    
vehiculo=Vehiculo("Azul", 4)
print(vehiculo)
coche=Coche("Rojo", 4, 50)
print(coche)
bicicleta=Bicicleta("Naranja", 2, "Urbano")
print(bicicleta)
        
    