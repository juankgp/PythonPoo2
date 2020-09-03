import sqlite3

def crearBDD():
    conexion = sqlite3.connect("piezas.db")
    cursor = conexion.cursor()

    try :
        cursor.execute('''CREATE TABLE piezas(
            pie_codigo integer primary key autoincrement,
            pie_nombre varchar(15) not null,
            pie_descripcion varchar(15) not null,
            pie_tipo varchar(13) not null
        ''')#se usa ''' para asegurar que sea cadena
    except sqlite3.OperationalError:
        print("La tabla ya existe")
    else:
        print("La tabla piezas se a creado satisfactoriamente")z

    try :
        cursor.execute('''CREATE TABLE proveedor(
            pro_codigo integer primary key autoincrement,
            pro_nombre varchar(15) not null,
            pro_direccion varchar(25) not null,
            pro_credito char(1)
            
        ''')#se usa ''' para asegurar que sea cadena
    except sqlite3.OperationalError:
        print("La tabla ya existe")
    else:
        print("La tabla proveedor se a creado satisfactoriamente")

    try :
            cursor.execute('''CREATE TABLE suministra(
                sum_codigo integer primary key autoincrement,
                sum_precio double not null,
                pie_codigo integer not null,
                foreign key(pie_codigo) references piezas(pie_codigo))
                pro_codigo integer not null,
                foreign key(pro_codigo) references suministra(sum_codigo))
                
            ''')#se usa ''' para asegurar que sea cadena
        except sqlite3.OperationalError:
            print("La tabla ya existe")
        else:
            print("La tabla siministra se a creado satisfactoriamente")
    

    conexion.commit()
    conexion.close()

def agregarEmpleado():
    enombre = input("Ingrese el nombre del Empleado\n")
    eapellidos = input("Ingrese los apellidos de l Emleado\n")
    ecedula = input("Ingrese la cédula del Empleado\n")
    eedad = int(input("ingre la edad del empleado\n"))
    eestado = input("Ingrese el estado\n")

    conexion = sqlite3.connect("empleado.db")
    cursor = conexion.cursor()

    #ejecutar sentecia insert
    try:
        cursor.execute("insert into empleado values(null , '{}', '{}','{}',{},'{}')".format(enombre,eapellidos,
        ecedula,eedad,eestado))
    except sqlite3.IntegrityError:
        print("Registro  '{}' ya existe ".format(enombre))
    else:
        print("Registro '{}' creado correctamente".format(enombre))
    
    conexion.commit()
    conexion.close()

def agregarPrestamo():
    conexion = sqlite3.connect("empleado.db")
    cursor = conexion.cursor()

    vempleado = cursor.execute("Select * from empleado ").fetchall()
    print("Cual es el id del empleado para realizar el prestamo")
    for emp in vempleado:
        print("{} {} ".format(emp[0],emp[1]))
    pempleado = int(input(""))
    pfecha = input("Ingrese la fecha de solicitud del prestamo\n")
    pvalor = input("Ingrese el valor del prestamo\n")
    pplazo = input("Ingrese el plazo esperado\n")

    try:
        cursor.execute("insert into prestamo values(null , '{}', {},'{}',{})".format(pfecha,pvalor,
        pplazo,pempleado))
    except sqlite3.IntegrityError:
        print("Registro  '{}' ya existe ".format(pempleado))
    else:
        print("Registro '{}' creado correctamente".format(pempleado))
    conexion.commit()
    conexion.close()

def consulta():
    conexion = sqlite3.connect("empleado.db")
    cursor = conexion.cursor()
    vempleado = cursor.execute("select * from empleado").fetchall()

    for emp in vempleado:
        print("Nombres: " + emp[1])
        print("Apellidos: " + emp[2])
        print("Cedula: " + emp[3])
        print("Edad: " + str(emp[4]))
        
        vprestamo = cursor.execute("select * from prestamo where emp_codigo={}".format(emp[0])).fetchall()

        for pres in vprestamo:
            print("Valor: {} ".format(pres[2]))
            print("Plazo: {}".format(pres[3]))
    conexion.commit()
    conexion.close()    
        
##llamar a metodo crear bd
crearBDD()
while True:
    print("Menu de opciones")
    opcion = input(
        "\n 1: Agregar empleado"
        "\n 2: Agregar prestamo"
        "\n 3: Mostrar prestamo"
        "\n 4: Salir\n"
    )
    if opcion == '1':
        agregarEmpleado()
    if opcion == '2':
        agregarPrestamo()
    if opcion == '3':
        consulta()
        