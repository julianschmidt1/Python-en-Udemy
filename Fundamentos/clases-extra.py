class Persona:
    def __init__(this, n, e, *t, **d): #atributo * tupla, ** diccionario
        this.nombre=n
        this.edad=e
        this.tupla=t
        this.diccionario=d
        
    def mostrar(this): #metodo mostrar
        print("El nombre es: ", this.nombre)
        print("La edad es: ", this.edad)
        print("Tupla ", this.tupla)
        print("Diccionario: ", this.diccionario)
        
p1= Persona("Julian", 20)
p1.mostrar()
print( )

p2= Persona("Guillermo", 27, 5,8,2, cp="Castaño", co="Marrón")
p2.mostrar()