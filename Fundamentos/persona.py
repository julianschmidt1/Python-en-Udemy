class Persona:
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad
#Modificar valores 
Persona.nombre="Julian"
Persona.edad="20"
#ver valores
print(Persona.nombre)
print(Persona.edad)
#crear objeto
persona=Persona("Javier","22")
print(persona.nombre)
print(persona.edad)
print(id(persona))

#objeto 2
personaDos=Persona("Guillermo", "28")
print(personaDos.nombre)
print(personaDos.edad)
print(id(personaDos))