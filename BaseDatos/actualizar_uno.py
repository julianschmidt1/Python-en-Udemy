import psycopg2

conexion=psycopg2.connect(user='postgres',
                          password='admin',
                          host='127.0.0.1',
                          port='5432',
                          database='test_db')

cursor=conexion.cursor()
sen1='UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona =  %s'
valores=("Jorge", "Perez", "jperez@gmail.com", 1)
cursor.execute(sen1, valores)
conexion.commit()
registros_actualizados=cursor.rowcount
print(f'Registros actualizados: {registros_actualizados}')
cursor.close()
conexion.close()