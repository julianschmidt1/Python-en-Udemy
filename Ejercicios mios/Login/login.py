from getpass import getpass

print("Registre sus credenciales.")
usernameR=input("Registre su nombre de usuario: ")
passwordR=getpass("Registre su contraseña: ")

print("Iniciar sesion")

username=input("Ingrese su nombre de usuario: ")
while username!=usernameR:
    username=input("Error. El nombre de usuario no esta registrado. Vuelva a ingresarlo: ")
password=getpass("Ingrese su contraseña: ")
while password!=passwordR:
    password=getpass("Error. Su contraseña es erronea. Vuelva a ingresarla: ")
        
print("¡Bienvenido!")