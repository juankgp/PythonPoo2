import sqlite3

conexion = sqlite3.connect('instituto.db')

cursor = conexion.cursor()
cursor.execute("UPDATE usuario SET usu_nombre = 'jpalma',usu_mail='jpalma@ismac.com' WHERE usu_nombre='jgutierrez' ")
cursor.execute("SELECT * FROM usuario")
usuario = cursor.fetchall()#recuerar todos los registros
for row in usuario:
    print(row)
conexion.commit()
conexion.close()