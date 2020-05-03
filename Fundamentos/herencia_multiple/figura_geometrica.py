#ABC Abstact Base Class
from abc import ABC, abstractmethod

class FiguraGeometrica:
    def __init__(self, ancho, alto):
        self.__alto=alto
        self.__ancho=ancho
        
    def get_alto(self):
        return self.__alto
    
    def set_alto(self):
        self.__alto=alto
        
    def get_ancho(self):
        return self.__ancho
    
    def set_ancho(self):
        self.__ancho=ancho
        
    def __str__(self):
        return "\nEl alto es: " + str(self.get_alto()) + "\nEl ancho es: " + str(self.get_ancho())
    
    @abstractmethod
    def area(self):
        pass