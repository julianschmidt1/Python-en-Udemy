import psycopg2

conexion=psycopg2.connect(user='postgres',
                          password='admin',
                          host='127.0.0.1',
                          port='5432',
                          database='test_db')

cursor=conexion.cursor()
sen1='SELECT * FROM persona WHERE id_persona IN %s'
entrada=input("Ingrese las pks a buscar (separe con comas): ")
tupla=tuple(entrada.split(','))
print(tupla)
pks = (tupla,)
cursor.execute(sen1, pks)
registros=cursor.fetchall()
for registro in registros:
    print(registro)

cursor.close()
conexion.close()