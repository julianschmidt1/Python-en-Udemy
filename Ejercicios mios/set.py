#set es una coleccion sin orden y sin id, ni elementos repetidos. Elementos no se pueden moficiar, si add o remov
planetas={"Marte","Jupiter","Venus"}
print(planetas)
#largo
print(len(planetas))
#ver si hay un elemento
print("Marte" in planetas)
#add
planetas.add("Tierra")
print(planetas)
#remove
planetas.remove("Tierra")
print(planetas)
#discard
planetas.discard("Jupiter")
print(planetas)
#clearear set
planetas.clear()
print(planetas)
#delete set
del planetas
print(planetas)