class Orden:
    contadorOrden=0
    
    def __init__(self, computadoras):
        Orden.contadorOrden+=1
        self.__id_orden=Orden.contadorOrden
        self.__computadoras=computadoras
        
    def agregar_pc(self, computadora):
        self.__computadoras.append(computadora)
        
    def __str__(self):
        computadora_str=""
        for computadora in self.__computadoras:
            computadora_str+=computadora.__str__()
            
        return(
            f"Orden: {self.__id_orden}, "
            f"Computadoras: {computadora_str}"
        )