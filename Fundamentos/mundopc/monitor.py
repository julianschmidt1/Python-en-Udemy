class Monitor:
    contadorMonitor=0
    
    def __init__(self, marca, tamanio):
        Monitor.contadorMonitor+=1
        self.__id_monitor=Monitor.contadorMonitor
        self.__marca=marca
        self.__tamanio=tamanio
        
    def __str__(self):
        return (
            f"Id: {self.__id_monitor}, "
            f"Marca: {self.__marca}, "
            f"Tamaño: {self.__tamanio}"
        )
    
