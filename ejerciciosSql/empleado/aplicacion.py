import tkinter as tk
from tkinter import messagebox as mb
import sqlite3
import sys


class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.ventana1.geometry('800x700')
        self.ventana1.title("Sistema de Prestamos")
        imagen = tk.PhotoImage(file="prestamo.png")
        tk.Label(self.ventana1,image=imagen,bd=0,width=380 , height =350).pack(side="top")
        self.agregarMenu()
        self.ventana1.mainloop()

    
    def agregarMenu(self):
        self.menubar1 = tk.Menu(self.ventana1)
        self.ventana1.config(menu = self.menubar1)
        self.archivo = tk.Menu(self.menubar1,tearoff = 0)
        self.sistemaM = tk.Menu(self.menubar1,tearoff = 0)
        ####################SubMenus###################################################
        ###########Archivo###############
        self.archivo.add_command(label="Crear base de Datos",command=self.crearBDD)
        self.archivo.add_command(label="Salir",command=self.Salir)
        #########Sitemas############33
        self.sistemaM.add_command(labe="Formulario Empleados",command=self.formEmpleados)
        ################################# Menus ###############################3
        self.menubar1.add_cascade(label="Archivo",menu=self.archivo)#creo el menu archivo
        self.menubar1.add_cascade(label="Sistemas",menu=self.sistemaM)#creo el menu archivo
    
    def formEmpleados(self):
        frame = tk.Frame(self.ventana1)
        frame.pack()
        self.emp_codigo = tk.StringVar()
        self.emp_nombres = tk.StringVar()
        self.emp_apellidos = tk.StringVar()
        self.emp_cedula = tk.StringVar()
        self.emp_edad = tk.IntVar()
        self.emp_estado = tk.StringVar()

        cuadroID = tk.Entry(frame,textvariable=self.emp_codigo)
        cuadroID.grid(row=0,column=1,padx=10,pady = 10)

        cuadroNombre = tk.Entry(frame,textvariable=self.emp_nombres)
        cuadroNombre.grid(row=1,column=1,padx=10,pady = 10)

        cuadroApellido = tk.Entry(frame,textvariable=self.emp_apellidos)
        cuadroApellido.grid(row=2,column=1,padx=10,pady = 10)

        cuadroCedula = tk.Entry(frame,textvariable=self.emp_cedula)
        cuadroCedula.grid(row=3,column=1,padx=10,pady = 10)

        cuadroEdad = tk.Entry(frame,textvariable=self.emp_edad)
        cuadroEdad.grid(row=4,column=1,padx=10,pady = 10)

        cuadroEstado = tk.Entry(frame,textvariable=self.emp_estado)
        cuadroEstado.grid(row=5,column=1,padx=10,pady = 10)

    def Salir(self):
        respuesta = mb.askyesno("Salir","Esta seguro de salir del sistema")
        if respuesta == True:
            sys.exit()
    def crearBDD(self):
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
            #print("La tabla ya existe")
            mb.askokcancel("Advertencia","La tabla ya existe")
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
            
aplicacion1 = Aplicacion()
