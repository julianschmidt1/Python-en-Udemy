from empleado import Empleado
from gerente import Gerente

def imprimir_detalles(tipo_padre):
    print(tipo_padre, end="\n\n")
    
empleado=Empleado("Julian", 5000)
imprimir_detalles(empleado)

empleado=Gerente("Sofia", 10000, "Tecnología")
imprimir_detalles(empleado)