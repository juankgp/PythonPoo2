import sqlite3

conexion = sqlite3.connect('instituto.db')

cursor = conexion.cursor()
cursor.execute("insert into usuario values (6,'dmonacayo','dmoncayo@ismac.com','123')")
conexion.commit()
conexion.close()

