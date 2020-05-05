from getpass import getpass

class Datos:
    
    def __init__(self, username, password):
        self.username=username
        self.password=password
    
    def pedirDatos(self, username, password):
        usernameR=input("Registre su nombre de usuario: ")
        passwordR=getpass("Registre su contraseña: ")