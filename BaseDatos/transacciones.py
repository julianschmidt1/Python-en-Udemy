import psycopg2 as db

conexion=db.connect(user='postgres',
                          password='admin',
                          host='127.0.0.1',
                          port='5432',
                          database='test_db')
try:
    #conexion.autocommit = True
    cursor=conexion.cursor()
    sen1='INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
    valores=("Julian", "Schmidt", "jschmidt@gmail.com")
    cursor.execute(sen1, valores)

    sen1='UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona =  %s'
    valores=("Javier", "Schmidt", "jschmidt@gmail.com", 9)
    cursor.execute(sen1, valores)

    conexion.commit()
except Exception as e:
    conexion.rollback(  )
    print(f'Ocurrio un error de transacción: {e}')
finally:
    cursor.close()
    conexion.close()