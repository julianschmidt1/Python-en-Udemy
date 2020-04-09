class Caja:
    def __init__(self, alto, ancho, largo): #atributos
        self.alto=alto
        self.ancho=ancho
        self.largo=largo
    
    #metodo Calcular Volumen
    def calcularVolumen(self):
        return alto*ancho*largo
    
alto=int(input("Ingrese el alto de la caja: "))
ancho=int(input("Ingrese el ancho de la caja: "))
largo=int(input("Ingrese el largo de la caja: "))

caja=Caja(alto, ancho, largo)
print("El volumen de la caja es: ", caja.calcularVolumen())