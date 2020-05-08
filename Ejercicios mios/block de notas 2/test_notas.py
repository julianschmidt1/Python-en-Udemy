from dominio.notas import Notas
from servicio.block_notas import BlockNotas

opcion=None
while opcion!="4":
    print(" - - - Opciones - - -")
    print("1. Agregar nota")
    print("2. Ver mis notas")
    print("3. Eliminar notas")
    print("4. Salir")
    opcion=input("Ingrese su opcion (1-4): ")
    if opcion=="1":
        agregarnota=input("Ingrese su nota: ")
        nota=Notas(agregarnota)
        BlockNotas.add_nota(nota)
    elif opcion=="2":
        BlockNotas.show_nota()
    elif opcion=="3":
        BlockNotas.delNota()
    else:
        print("Nos veeeeeemoooooooooooooooooooos")