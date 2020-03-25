#compuesto por llave, valor (key,value)
diccionario={
    "IDE": "Integrated Development Enviroment",
    "OOP": "Objet Oriented Programming",
    "DBMS": "Database Management System"
}
print(diccionario)
#largo
print(len(diccionario))
#acceder a un elemento
print(diccionario["IDE"])
print(diccionario.get("IDE"))
#modificar valores
diccionario["IDE"]="Integrated development enviroment"
print(diccionario)
#iterar
for termino in diccionario:
    print(termino)
    
for termino in diccionario:
    print(diccionario[termino])
    
for valor in diccionario.values():
    print(valor)
    
#comprobar existencia
print("IE" in diccionario)

#agregar elementos
diccionario["PK"]="Primary Key"
print(diccionario)

#eliminar
diccionario.pop("DBMS")
print(diccionario)

#clear
diccionario.clear()
print(diccionario)

#eliminar var
del diccionario