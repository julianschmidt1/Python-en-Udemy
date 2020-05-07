import os

class BlockNotas:
    
    ruta_archivo="notas.txt"
    
    @staticmethod
    def agregar_nota(nota):
        try:
            archivo=open(BlockNotas.ruta_archivo,"a")
            archivo.write(nota.__str__() + "\n")
        except Exception as e:
            print("Error al agregar: ",e)
        finally:
            archivo.close()
            
    @staticmethod
    def mostrar_nota():
        try:
            archivo = open(BlockNotas.ruta_archivo, "r")
            print("\n- - - - - NOTAS - - - - -\n")
            print(archivo.read())
        except Exception as e:
            print("Error al mostrar notas.", e)
        finally:
            archivo.close()
            
    @staticmethod   
    def eliminarnota():
        try:
            os.remove(BlockNotas.ruta_archivo)
            print("\nHistorial eliminado.")
        except Exception as e:
            print("Error al eliminar historial.")