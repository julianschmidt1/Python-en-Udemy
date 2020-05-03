from cuadrado import Cuadrado
from rectangulo import Rectangulo
from figura_geometrica import FiguraGeometrica

cuadrado=Cuadrado(2, "Verde")
print("- - - - Caracteristicas del cuadrado - - - -", cuadrado)
print("El area es:",cuadrado.area())
rectangulo=Rectangulo(4, "Azul")
print("- - - - Caracteristicas del rectangulo - - - -", rectangulo)
print("El area es : ",rectangulo.area())