#Tupla, mantiene orden pero no se puede modfiicar
perifericos=("Mouse", "Teclado", "Monitor")
print(perifericos)
#Largo de la tupla
print(len(perifericos))
#Acceder a elemento
print(perifericos[0])
#Rango
print(perifericos[0:2]) #excluye el 2

#modificar valores--> se convierte la tupla en lista, se modifica el id indicado, y se vuelve a convertir a tupla.
perifericosLista=list(perifericos)
perifericosLista[0]="Mousecito"
perifericos=tuple(perifericosLista)
print(perifericos)

#iterar tupla
for periferico in perifericos:
    print(periferico, end=" ")