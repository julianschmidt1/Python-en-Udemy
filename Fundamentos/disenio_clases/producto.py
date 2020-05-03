class Producto:
    contador_productos=0
    
    def __init__(self, nombre, precio):
        Producto.contador_productos +=1
        self.__id_producto = Producto.contador_productos
        self.__nombre=nombre
        self.__precio=precio
        
    def get_precio(self):
        return self.__precio
        
    def __str__(self):
        return "\nID producto: "+ str(self.__id_producto) + "\nNombre: " + self.__nombre + "\nPrecio: " + str(self.__precio)