from dispositivos_entrada import DispositivoEntrada

class Teclado(DispositivoEntrada):
    contadorTeclado=0
    
    def __init__(self, marca, tipo_entrada):
        Teclado.contadorTeclado+=1
        self.__id_teclado=Teclado.contadorTeclado
        self._marca=marca
        self._tipo_entrada=tipo_entrada
        
    def __str__(self):
        return (
            f"Id: {self.__id_teclado}, "
            f"Marca: {self._marca}, "
            f"Tipo de entrada: {self._tipo_entrada}"
        )
        
