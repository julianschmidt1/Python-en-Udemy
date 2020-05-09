import psycopg2

conexion=psycopg2.connect(user='postgres',
                          password='admin',
                          host='127.0.0.1',
                          port='5432',
                          database='test_db')

cursor=conexion.cursor()
sen1='DELETE FROM persona WHERE id_persona IN %s'
entrada=input("Ingrese el pk a eliminar: ")
tupla=tuple(entrada.split(','))
valores=(tupla,)
cursor.execute(sen1, valores)
conexion.commit()
registros_eliminados=cursor.rowcount
print(f'Registros eliminados: {registros_eliminados}')
cursor.close()
conexion.close()