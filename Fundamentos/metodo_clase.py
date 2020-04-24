class Clase:
    
    variable_clase="Variable de clase"
    
    def __init__(self):
        self.variable_instancia="Variable de instancia"
        
    #Desde metodos estaticos o de clase no se puede acceder a var de instancia
    
    @staticmethod #decorador
    def metodo_estatico():
        print("Metodo estatico") #no recibo parametros, no se adquieren cosas de clase
        print(Clase.variable_clase)
        
    @classmethod
    def metodo_clase(cls): #se recibe cls y se puede acceder a la clase
        print("Metodo de clase", str(cls))
        print(cls.variable_clase)
        
    def metodo_instancia(self): #se ejecutan mediante objetos
        self.metodo_clase()
        self.metodo_estatico()
        
Clase.metodo_estatico()
Clase.metodo_clase()

print()
objeto1=Clase()
objeto1.metodo_instancia()