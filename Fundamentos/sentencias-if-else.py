condicion=input("Indique si la condición es verdadera o falsa (V/F): ")
if condicion == "V":
    print("La condicion es verdadera.")
elif condicion == "F":
    print("La condicion es falsa.")
else:
    print("La condicion no se reconoce.")
    
numero=int(input("Ingrese un numero entre 1 y 3: "))
if numero==1:
    numeroTexto="numero uno"
elif numero==2:
    numeroTexto="numero dos"
elif numero==3:
    numeroTexto="numero tres"
else:
    numeroTexto="Error. El numero ingresado no es valido."
print("El numero que ingresaste es: ", numeroTexto)