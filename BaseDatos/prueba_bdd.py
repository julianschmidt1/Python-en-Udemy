import psycopg2

conexion=psycopg2.connect(user='postgres',
                          password='admin',
                          host='127.0.0.1',
                          port='5432',
                          database='test_db')

cursor=conexion.cursor()
sen1='SELECT * FROM persona ORDER BY id_persona'
cursor.execute(sen1)
registro=cursor.fetchall()
print(registro)

cursor.close()
conexion.close()