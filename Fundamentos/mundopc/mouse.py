from dispositivos_entrada import DispositivoEntrada

class Mouse(DispositivoEntrada):
    contadorMouse=0
    
    def __init__(self, marca, tipo_entrada):
        Mouse.contadorMouse+=1
        self.__id_mouse=Mouse.contadorMouse
        self._marca=marca
        self._tipo_entrada=tipo_entrada
        
    def __str__(self):
        return (
            f"Id: {self.__id_mouse}, "
            f"Marca: {self._marca}, "
            f"Tipo de entrada: {self._tipo_entrada}"
        )
        
