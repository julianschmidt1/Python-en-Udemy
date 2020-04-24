class Clase:
    variable_clase="var de clase"
    
    def __init__(self, variable_instancia):
        self.variable_instancia=variable_instancia
        
print(Clase.variable_clase)
ob1=Clase("Var uwu")
Clase.variable_instancia="Isi bobo"
print(Clase.variable_instancia) #valor diferente
print(ob1.variable_instancia) #valor diferente

ob1.variable_clase="Cambio"
print(ob1.variable_clase)
print(Clase.variable_clase)

ob2=Clase("Valor aa")
print(ob2.variable_clase)