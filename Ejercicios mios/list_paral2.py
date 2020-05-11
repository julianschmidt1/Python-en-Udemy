nombre = []
nota = []



for c in range(4):
    #nom = input("Ingrese el nombre del alumno: ")
    #nombre.append(nom)
    no = int(input("Ingrese la nota del alumno: "))
    nota.append(no)

mayores=0
for x in range(4):
    #print(nombre[x])
    print(nota[x])
    if nota[x]>=8:
        print("Muy bueno")
        mayores+=1
    elif nota[x]>=4:
        print("Bueno")
    else:
        print("Insuficiente")
print("La cantidad de notas mayores a 8 es : ",mayores)

