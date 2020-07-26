import sqlite3

def crearBDD():
    conexion = sqlite3.connect("empleado.db")
    cursor = conexion.cursor()

    try :
        cursor.execute('''CREATE TABLE empleado(
            emp_codigo integer primary key autoincrement,
            emp_nombres varchar(15) not null,
            emp_apellidos varchar(15) not null,
            emp_cedula varchar(13) not null,
            emp_edad int not null,
            emp_estado char(1) not null)
        ''')#se usa ''' para asegurar que sea cadena
    except sqlite3.OperationalError:
        print("La tabla ya existe")
    else:
        print("La tabla empleado se a creado satisfactoriamente")



    try :
        cursor.execute('''CREATE TABLE prestamo(
            pre_codigo integer primary key autoincrement,
            pre_fecha date not null,
            pre_valor double not null,
            pre_plazo varchar(20),
            emp_codigo integer not null,
            foreign key(emp_codigo) references empleado(emp_codigo))
        ''')#se usa ''' para asegurar que sea cadena
    except sqlite3.OperationalError:
        print("La tabla ya existe")
    else:
        print("La tabla prestamo se a creado satisfactoriamente")



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
        
        