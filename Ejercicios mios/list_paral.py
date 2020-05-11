nombre=[]
precio=[]
contador=0

for x in range(5):
    '''nom=input("Ingrese el nombre del producto: ")
    nombre.append(nom)'''
    pre=int(input("Ingrese el precio del producto: "))
    precio.append(pre)
    
for c in range(1,5):
    if precio[c]>precio[0]:
        contador+=1
        
print("La cantidad de productos mayores al primer producto es de: ",contador)