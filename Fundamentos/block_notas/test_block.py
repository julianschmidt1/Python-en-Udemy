from dominio.notas import Notas
from servicio.block_notas import BlockNotas

opcion=None
while opcion != "4":
    print("\n- - - - Menu principal - - - -\n")
    print("1- Agregar nota.")
    print("2- Ver notas.")
    print("3- Eliminar historial.")
    print("4- Salir")
    opcion=input("Escriba su opcion (1-4): ")
    if opcion=="1":
        agregar=input("Ingrese su nota: ")
        nota=Notas(agregar)
        BlockNotas.agregar_nota(nota)
    elif opcion=="2":
        BlockNotas.mostrar_nota()
    elif opcion=="3":
        BlockNotas.eliminarnota()
        
else:
    print("Fin del programa")