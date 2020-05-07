try:
    archivo=open("prueba.txt", "w")
    archivo.write("Agrego info al archivo\n")
    archivo.write("jjsj")
except Exception as e:
    print(e)
finally:
    archivo.close()