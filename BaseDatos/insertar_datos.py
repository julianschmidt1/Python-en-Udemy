import psycopg2

conexion=psycopg2.connect(user='postgres',
                          password='admin',
                          host='127.0.0.1',
                          port='5432',
                          database='test_db')

cursor=conexion.cursor()
sen1='INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
valores=("Guillermo", "Schmidt", "gschmidt@gmail.com")
cursor.execute(sen1, valores)
conexion.commit()
registros_insertados=cursor.rowcount
print(f'Registros insertados: {registros_insertados}')
cursor.close()
conexion.close()