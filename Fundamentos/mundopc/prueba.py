from orden import Orden
from computadora import Computadora
from monitor import Monitor
from teclado import Teclado
from mouse import Mouse

tecladoRaz=Teclado("Razer", "USB")
mouseRaz=Mouse("Razer", "USB")
monitorHP=Monitor("HP", "25 pulgadas")
computadoraGamer=Computadora("Gamer", monitorHP, tecladoRaz, mouseRaz)

tecladoLogi=Teclado("Logitech", "USB")
mouseLogi=Mouse("Logitech", "USB")
monitorHP=Monitor("HP", "30 pulgadas")
computadoraLab=Computadora("Trabajo", monitorHP, tecladoLogi, mouseLogi)

computadoras1=[computadoraGamer, computadoraLab]
orden1=Orden(computadoras1)
print(orden1)

computadoras2=[computadoraGamer, computadoraGamer]
orden2=Orden(computadoras2)
print(orden2)