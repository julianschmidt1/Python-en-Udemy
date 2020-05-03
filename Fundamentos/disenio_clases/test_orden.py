from producto import Producto
from orden import Orden

producto1= Producto("Remera", 250)
producto2= Producto("Pantalon", 200)
producto3= Producto("Gorro", 75)

productos=[producto1, producto2]

orden1=Orden(productos)
print(orden1)

orden2=Orden(productos)
orden2.agregar_producto(producto3)
print(orden2)
print("El total es: ",orden2.calcular_total())