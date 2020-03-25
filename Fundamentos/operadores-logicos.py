#a=int(input("Ingrese un valor entre 0 y 5: "))
a=3
valorMinimo=0
valorMaximo=5
dentroRango= a>=valorMinimo and a<=valorMaximo
print(dentroRango)

if(dentroRango):
    print("El valor ingresado se encuentra dentro del rango.")
else:
    print("El valor ingresado no se encuentra dentro del rango.")

vacaciones=False
diaDescanso=True
if(not(vacaciones or diaDescanso)):
    print("No odes salir a pasear")
else:
    print("Podes ir al parque uwu.")