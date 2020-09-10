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
       
        ####################SubMenus###################################################
        ###########Archivo###############
        self.archivo.add_command(label="Crear base de Datos",command=self.crearBDD)
        self.archivo.add_command(label="Salir",command=self.Salir)
        
        #########Sitemas############33
        self.sistemaM = tk.Menu(self.menubar1,tearoff = 0)
        self.sistemaM.add_command(labe="Formulario Empleados",command=self.formEmpleados)
        self.sistemaM.add_command(labe="Limpiar Campos",command=self.limpiarCampos)
        #############Operaciones##############3
        self.operacionesMenu = tk.Menu(self.menubar1,tearoff = 0)
        self.operacionesMenu.add_command(labe="Agregar",command=self.agregaEmp)
        ################################# Menus ###############################3

        self.menubar1.add_cascade(label="Archivo",menu=self.archivo)#creo el menu archivo
        self.menubar1.add_cascade(label="Sistemas",menu=self.sistemaM)#creo el menu archivo
        self.menubar1.add_cascade(label="Operaciones",menu=self.operacionesMenu)#creo el menu archivo
    
    def formEmpleados(self):
        #frame = tk.Frame(self.ventana1)
        vempleado = tk.Toplevel(self.ventana1)
        frame=tk.Frame(vempleado)
        frame.config(bg="blue")

        frame.pack()

        ##Formato formulario
        mi_label = tk.Label(vempleado,text="empleado")
        mi_label.pack(side=tk.LEFT)
        mi_label.config(font=("Arial",14))
        mi_label.config(fg="blue")
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

        #etiquetas

        idLabel = tk.Label(frame,text="Código: ")
        idLabel.grid(row=0,column=0)
        nombresLabel = tk.Label(frame,text="Nombres: ")
        nombresLabel.grid(row=1,column=0)
        apellidosLabel = tk.Label(frame,text="Apellidos: ")
        apellidosLabel.grid(row=2,column=0)
        cedulaLabel = tk.Label(frame,text="Cedula: ")
        cedulaLabel.grid(row=3,column=0)
        edadLabel = tk.Label(frame,text="Edad: ")
        edadLabel.grid(row=4,column=0)
        estadoLabel = tk.Label(frame,text="Estado: ")
        estadoLabel.grid(row=5,column=0)

        #botones
        frame2 = tk.Frame(vempleado)
        frame2.pack()
        botonCreate=tk.Button(frame2,text="Agregar",command=self.agregaEmp)
        botonCreate.grid(row=0,column=0,padx=10,pady=10)

        botonRead=tk.Button(frame2,text="Consultar",command=self.consultarEmp)
        botonRead.grid(row=0,column=1,padx=10,pady=10)

        botonUpdate=tk.Button(frame2,text="Actualizar",command=self.actualizarEmp)
        botonUpdate.grid(row=0,column=2,padx=10,pady=10)

        botonDelete=tk.Button(frame2,text="Borrar",command=self.eliminarEmp)
        botonDelete.grid(row=0,column=3,padx=10,pady=10)
    
    def agregaEmp(self):
        conexion = sqlite3.connect('empleado.db')
        cursor = conexion.cursor()
        try:
            datos=self.emp_codigo.get(), self.emp_nombres.get(),self.emp_apellidos.get(),self.emp_cedula.get(),self.emp_edad.get(),self.emp_estado.get()
            cursor.execute("insert into empleado values(? , ? , ? , ?, ? , ?)",datos)
        except sqlite3.IntegrityError:
            print("Registro  '{}' ya existe ".format(self.emp_codigo.get()))
        else:
            print("Registro '{}' creado correctamente".format(self.emp_codigo.get()))
        tk.messagebox.showinfo("Base de Datos", "Registro insertado con exito")
        conexion.commit()
        conexion.close()


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

    def consultarEmp(self):
        conexion = sqlite3.connect("empleado.db")
        cursor = conexion.cursor()
        cursor.execute("Select * from empleado where emp_codigo=" + self.emp_codigo.get())
        empleado = cursor.fetchall()

        for e in empleado:
            self.emp_codigo.set(e[0])
            self.emp_nombres.set(e[1])
            self.emp_apellidos.set(e[2])
            self.emp_cedula.set(e[3])
            self.emp_edad.set(e[4])
            self.emp_estado.set(e[5])
        conexion.commit()
        conexion.close()
    def actualizarEmp(self):
        conexion = sqlite3.connect('empleado.db')
        cursor = conexion.cursor()
        
        datos=self.emp_nombres.get(),self.emp_apellidos.get(),self.emp_cedula.get(),self.emp_edad.get(),self.emp_estado.get()
        cursor.execute("update empleado set emp_nombres=?, emp_apellidos=? ,emp_cedula=? , emp_edad=? , emp_estado=?"+"where emp_codigo="+ self.emp_codigo.get(),datos )
        
        tk.messagebox.showinfo("Base de Datos", "Registro actualizado con exito")
        conexion.commit()
        conexion.close()

    def eliminarEmp(self):
        conexion = sqlite3.connect('empleado.db')
        cursor = conexion.cursor()
        cursor.execute("delete from empleado where emp_codigo="+self.emp_codigo.get())
        tk.messagebox.showinfo("Base de Datos", "Registro eliminado con exito")
        conexion.commit()
        conexion.close()

    def limpiarCampos(self):
        self.emp_codigo.set("");
        self.emp_nombres.set("")
        self.emp_apellidos.set("")
        self.emp_cedula.set("")
        self.emp_edad.set(0)
        self.emp_estado.set("")
aplicacion1 = Aplicacion()
