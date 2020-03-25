print("Proporcione los siguientes datos del libro: ") #nombre, id, precio, enviogratuito
nombre=input("Ingrese el nombre: ")
id=int(input("Ingrese el id: "))
precio=float(input("Ingrese el precio: "))
envioGratuito=input("Ingrese si el envio es gratuito o no. (SI/NO) ")

if envioGratuito == "SI":
    envioGratuito = "El envio es gratuito."
elif envioGratuito == "NO":
    envioGratuito = "El envio debe ser pagado."
else:
    envioGratuito=("La opcion ingresada no es válida, por favor indique la opcion con SI/NO.")

print("Nombre: ",nombre)
print("ID: ",id)
print("Precio: ",precio)
print("¿Envio gratuito? ",envioGratuito)