import psycopg2

conexion=psycopg2.connect(user='postgres',
                          password='admin',
                          host='127.0.0.1',
                          port='5432',
                          database='test_db')

cursor=conexion.cursor()
sen1='SELECT * FROM persona WHERE id_persona = %s'
id_persona=input("Ingrese la PK a buscar: ")
pk=(id_persona,)
cursor.execute(sen1, pk)
registro=cursor.fetchone()
print(registro)

cursor.close()
conexion.close()