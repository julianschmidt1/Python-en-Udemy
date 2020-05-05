class Persona():
    pass

persona=Persona()

first_key='Ndea'
first_val='Dou'

setattr(persona, first_key, first_val)
first=getattr(persona, first_key)

print(first)