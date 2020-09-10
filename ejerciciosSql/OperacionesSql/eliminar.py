import sqlite3

conexion = sqlite3.connect('instituto.db')

cursor = conexion.cursor()
cursor.execute("Delete from usuario WHERE usu_codigo=1 ")
cursor.execute("SELECT * FROM usuario")
usuario = cursor.fetchall()#recuperar todos los registros
for row in usuario:
    print(row)
conexion.commit()
conexion.close()