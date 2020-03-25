nota=int(input("Ingrese la calificacion del estudiante: (0/10) "))

if nota == 10 or nota == 9:
    nota="A"
elif nota < 9 and nota >= 8:
    nota="B"
elif nota < 8 and nota >= 7:
    nota="C"
elif nota < 7 and nota >= 6:
    nota="D"
elif nota < 6 and nota >= 0:
    nota="F"
else:
    print("La calificacion ingresada no es válida.")
print(nota)