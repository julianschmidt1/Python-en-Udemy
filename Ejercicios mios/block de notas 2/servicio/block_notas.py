import os

class BlockNotas:
    ruta="prueba.txt"
    
    @staticmethod
    def add_nota(nota):
        try:
            archivo=open(BlockNotas.ruta, "a")
            archivo.write(nota.__str__() + "\n")
        except Exception as e:
            print("Hubo un error al agregar la nota.", e)
        finally:
            archivo.close()
            
    @staticmethod
    def show_nota():
        try:
            archivo=open(BlockNotas.ruta, "r")
            print("- - - - Tus notas - - - -")
            print(archivo.read())
        except Exception as e:
            print("Ocurrio un error al mostrar tus notas",e)
        finally:
            archivo.close()
            
    @staticmethod
    def delNota(nota):
        try:
            os.remove(BlockNotas.ruta)
            print("Historial de notas eliminado")
        except Exception as e:
            print("Ocurrio un error al eliminar tus notas", e)