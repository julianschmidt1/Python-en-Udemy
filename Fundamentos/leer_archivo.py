try:
    archivo=open("D:\Perfil de Usuario\Desktop\Python-en-Udemy\Fundamentos\prueba.txt", "r")
    #print(archivo.read()) 
    #print(archivo.read(6)) #leer caracteres
    #print(archivo.readline()) #leer linea
    
    #for linea in archivo: #iterar lineas
    #    print(linea)
    #print(archivo.readlines()[1]) #Lineas como lista
    archivoDos=open("copia.txt", "w")
    archivoDos.write(archivo.read())
    
except Exception as e:
    print(e)
finally:    
    archivo.close()
    archivoDos.close()
