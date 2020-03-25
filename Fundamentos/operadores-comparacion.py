a=3
b=2
resultado=a==b
print(resultado)

resultado= a != b
print(resultado)

resultado= a>b
print(resultado)

resultado = a>=b
print(resultado)

resultado = a<b
print(resultado)

resultado = a<=b
print(resultado)

if a%2==0:
    print("Es un numero par.")
else:
    print("Es un numero impar.")
    
edadLimite=int(input("Ingrese la edad de la persona: "))
if edadLimite>=18:
    print("Es mayor de edad.")
else:
    print("No es mayor de edad.")