nombres=["Julian", "Javier", "Guillermo", "Romina"]
print(nombres)
#largo de la lista
print(len(nombres))
#elementos especificos
print(nombres[0])
print(nombres[1])
#navegacion negativa
print(nombres[-1])
print(nombres[-2])
#imprimir rango
print(nombres[0:2])
#imprimir elementos desde el inicio hasta el indice especifico
print(nombres[:3])
#imprimir elementos hasta el final desde indice especifico
print(nombres[1:])
#cambiar elementos de una lista
nombres[0]="Pablo"
print(nombres)
#iterar la lista
for nombre in nombres:
    print (nombre)
#Revisar si existe un elemento
if "Julian" in nombres:
    print("Julian si existe en la lista")
else:
    print("Julian no existe")