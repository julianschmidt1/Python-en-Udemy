from monitor import Monitor
from teclado import Teclado
from mouse import Mouse

class Computadora:
    contadorComputadora=0
    
    def __init__(self, nombre, monitor, teclado, mouse):
        Computadora.contadorComputadora+=1
        self.__id_computadora=Computadora.contadorComputadora
        self.__nombre=nombre
        self.__monitor=monitor
        self.__teclado=teclado
        self.__mouse=mouse
        
    def __str__(self):
        return (
            f"""
            {self.__nombre}: {self.__id_computadora}
                Monitor: {self.__monitor}
                Teclado: {self.__teclado}
                Mouse: {self.__mouse}
            """
        )