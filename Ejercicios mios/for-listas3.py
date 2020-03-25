tupla=(1,2,3,4,5,6,7,8,9,10,11,12,13)

lista=list(tupla)
for i in lista:
    if i%2==1:
        lista.remove(i)
print(lista)