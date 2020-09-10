import sqlite3

conexion = sqlite3.connect('instituto.db')
cursor = conexion.cursor()

#Recuperar los datos de una tabla
cursor.execute("SELECT * FROM usuario where usu_codigo=3")
usuario = cursor.fetchone()#recuerar un unico registro
print(usuario)
conexion.commit()
conexion.close()
