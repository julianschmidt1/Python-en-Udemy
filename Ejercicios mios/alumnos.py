import sys

class Alumnos:
    def __init__(self):
        self.nombres=[]
        self.notas=[]
        
    def menu(self):
        opcion=None
        while opcion!="4":
            print("\n---Opciones---\n")
            print("1. Cargar alumno: ")
            print("2. Listar alumnos: ")
            print("3. Mostrar mayores a 7: ")
            print("4. Salir del programa. ")
            opcion=(input("Ingrese su opcion: "))
            if opcion=="1":
                self.cargar_alumno()
            elif opcion=="2":
                self.listar_alumnos()
            elif opcion=="3":
                self.mayor_7()
            elif opcion=="4":
                sys.close()
                
    def cargar_alumno(self):
        for x in range(2):
            nom=input("Ingrese el nombre y apellido del alumno: ")
            self.nombres.append(nom)
            no=int(input("Ingrese la nota del alumno: "))
            self.notas.append(no)
            
    def listar_alumnos(self):
        print("Listado de alumnos: ")
        print("---------------------------------")
        for x in range(2):
            print(self.nombres[x], self.notas[x])
            
        
    def mayor_7(self):
        print("Alumnos mayores a 7")
        for x in range(2):
            if self.notas[x]>=7:
                print(self.nombres[x]," - ", self.notas[x])
                
obj1=Alumnos()
obj1.menu()