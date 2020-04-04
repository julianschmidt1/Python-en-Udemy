class Rectangulo:
    def __init__(self, base, altura):
        self.base=base
        self.altura=altura
        
    #CalcularArea
    def calcularArea(self):
        return self.base*self.altura

base=int(input("Ingrese la base del rectangulo: "))
altura=int(input("Ingrese la altura del rectangulo: "))

rectangulo=Rectangulo(base,altura)
print("El area del rectangulo es: ",rectangulo.calcularArea())