tupla=(1,3,5,9,6,12,15,22,45,11,6)
lista=[]

for i in tupla:
    if i>=5 and i<=15:
        lista.append(i)

print(lista)