class Perro:
    def __init__(self, humano, canino): #atributos
        self.humano=humano
        self.canino=canino
        
    def calcularEdad(self): #metodo
        return humano/canino
    
canino=7
humano=int(input("Ingrese su edad y será traducida a años perro: "))

perro=Perro(humano, canino)
print("Su edad perro es: ",perro.calcularEdad())