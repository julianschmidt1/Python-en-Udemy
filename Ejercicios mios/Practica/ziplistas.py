nombres=['Julian', 'Sofia', 'Romina']
apellidos=["Schmidt", "Belucci", "Cipollari"]
edad=["20", "18", "47"]
localidad=["Wilde", "Gerli", "Wilde"]

for nom, ape, años, viv in zip(nombres,apellidos,edad,localidad):
    print(f'El apellido de {nom} es {ape} y tiene {años} anios.\n Vive en {viv}\n')
    
for valor in zip(nombres,apellidos,edad,localidad):
    print(valor)