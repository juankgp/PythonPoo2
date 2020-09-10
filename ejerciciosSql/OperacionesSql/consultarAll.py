import sqlite3

conexion = sqlite3.connect('instituto.db')
cursor = conexion.cursor()

#Recuperar los datos de una tabla
cursor.execute("SELECT * FROM usuario")
usuario = cursor.fetchall()#recuerar todos los registros
#print(usuario)
for row in usuario:
    print(row)

for row in usuario:
    print(row[1],'\t',row[2])
conexion.commit()
conexion.close()
