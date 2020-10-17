import tkinter as tk
from tkinter import messagebox as mb
from functools import partial
from consultaPiezas import *
from consultaProveedor import *
from consultaInventario import *
import sqlite3
import sys


class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.ventana1.geometry('400x350')
        self.ventana1.title("Mi Ferretería")
        imagen = tk.PhotoImage(file="toolbox.png")
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
        self.sistemaM.add_command(labe="Ingreso de Piezas",command=self.formPiezas)
        self.sistemaM.add_command(labe="Ingreso de Proveedores",command=self.formProve)
        self.sistemaM.add_command(labe="Ingreso a Inventario",command=self.formInv)
        self.sistemaM.add_command(label="Consulta Piezas",command=ventanaReporte)
        self.sistemaM.add_command(label="Consulta Proveedores",command=ventanaProveedor)
        self.sistemaM.add_command(label="Consulta Inventario",command=ventanaInventario)
        self.sistemaM.add_command(labe="Limpiar Campos",command=self.limpiarCampos)
        #############Operaciones##############3
        self.operacionesMenu = tk.Menu(self.menubar1,tearoff = 0)
        self.operacionesMenu.add_command(labe="Agregar",command=self.agregaPieza)
        ################################# Menus ###############################3

        self.menubar1.add_cascade(label="Archivo",menu=self.archivo)#creo el menu archivo
        self.menubar1.add_cascade(label="Sistemas",menu=self.sistemaM)#creo el menu archivo
        self.menubar1.add_cascade(label="Operaciones",menu=self.operacionesMenu)#creo el menu archivo
   #########formulario pizas/////////////////////////// 
    def formPiezas(self):
        #frame = tk.Frame(self.ventana1)
        vpieza = tk.Toplevel(self.ventana1)
        vpieza.title("Ingreso de piezas")
        vpieza.config(bg="blue")
        mi_label = tk.Label(vpieza,text="Por favor Ingrese los Datos").pack(anchor = 'center')
        
        frame=tk.Frame(vpieza)
        
        frame.config(bg="blue")

        frame.pack()

        ##Formato formulario
        
        #mi_label.pack(side=tk.LEFT)
        #mi_label.config(font=("Arial",14))
        #mi_label.config(fg="blue")
        
        self.pie_codigo = tk.StringVar()
        self.pie_nombre = tk.StringVar()
        self.pie_descripcion = tk.StringVar()
        self.pie_tipo = tk.StringVar()
        

        cuadroID = tk.Entry(frame,textvariable=self.pie_codigo)
        cuadroID.grid(row=0,column=1,padx=10,pady = 10)

        cuadroNombre = tk.Entry(frame,textvariable=self.pie_nombre)
        cuadroNombre.grid(row=1,column=1,padx=10,pady = 10)

        cuadroDescripcion = tk.Entry(frame,textvariable=self.pie_descripcion)
        cuadroDescripcion.grid(row=2,column=1,padx=10,pady = 10)

        cuadroTipo = tk.Entry(frame,textvariable=self.pie_tipo)
        cuadroTipo.grid(row=3,column=1,padx=10,pady = 10)


        #etiquetas

        idLabel = tk.Label(frame,text="Código: ")
        idLabel.grid(row=0,column=0)
        nombresLabel = tk.Label(frame,text="Nombres: ")
        nombresLabel.grid(row=1,column=0)
        apellidosLabel = tk.Label(frame,text="Descripción: ")
        apellidosLabel.grid(row=2,column=0)
        cedulaLabel = tk.Label(frame,text="Tipo: ")
        cedulaLabel.grid(row=3,column=0)
        
        #botones
        frame2 = tk.Frame(vpieza)
        frame2.pack()
        botonCreate=tk.Button(frame2,text="Agregar",command=self.agregaPieza)
        botonCreate.grid(row=0,column=0,padx=10,pady=10)

        botonRead=tk.Button(frame2,text="Consultar",command=self.consultarPieza)
        botonRead.grid(row=0,column=1,padx=10,pady=10)

        botonUpdate=tk.Button(frame2,text="Actualizar",command=self.actualizarPieza)
        botonUpdate.grid(row=0,column=2,padx=10,pady=10)

        botonDelete=tk.Button(frame2,text="Borrar",command=self.eliminarPieza)
        botonDelete.grid(row=0,column=3,padx=10,pady=10)
    
    def agregaPieza(self):
        conexion = sqlite3.connect('piezas.db')
        cursor = conexion.cursor()
        try:
            datos=self.pie_codigo.get(), self.pie_nombre.get(),self.pie_descripcion.get(),self.pie_tipo.get()
            cursor.execute("insert into piezas values(? , ? , ? , ?)",datos)
        except sqlite3.IntegrityError:
            print("Registro  '{}' ya existe ".format(self.pie_codigo.get()))
            tk.messagebox.showinfo("Base de Datos", "Registro '{}' ya existe".format(self.pie_codigo.get()))
        else:
            print("Registro '{}' creado correctamente".format(self.pie_codigo.get()))
            tk.messagebox.showinfo("Base de Datos", "Registro insertado con exito")
        conexion.commit()
        conexion.close()

    def consultarPieza(self):
        conexion = sqlite3.connect("piezas.db")
        cursor = conexion.cursor()
        cursor.execute("Select * from piezas where pie_codigo=" + self.pie_codigo.get())
        piezas = cursor.fetchall()
        if not piezas:
            print("Lista vacia")
            self.pie_codigo.set("")
            self.pie_nombre.set("")
            self.pie_descripcion.set("")
            self.pie_tipo.set("")
            tk.messagebox.showinfo("Base de Datos", "No existe ese registro...")
       # print(piezas.count())
        for e in piezas:
            self.pie_codigo.set(e[0])
            self.pie_nombre.set(e[1])
            self.pie_descripcion.set(e[2])
            self.pie_tipo.set(e[3])
            
        conexion.commit()
        conexion.close()

    def actualizarPieza(self):
        conexion = sqlite3.connect('piezas.db')
        cursor = conexion.cursor()
        
        
        datos=self.pie_nombre.get(),self.pie_descripcion.get(),self.pie_tipo.get()
        cursor.execute("update piezas set pie_nombre=?, pie_descripcion=? ,pie_tipo=? "+"where pie_codigo="+ self.pie_codigo.get(),datos )
        
        tk.messagebox.showinfo("Base de Datos", "Registro actualizado con exito")
        conexion.commit()
        conexion.close()

    def eliminarPieza(self):
        conexion = sqlite3.connect('piezas.db')
        cursor = conexion.cursor()
        cursor.execute("delete from piezas where pie_codigo="+self.pie_codigo.get())
        tk.messagebox.showinfo("Base de Datos", "Registro eliminado con exito")
        conexion.commit()
        conexion.close()
###Formulario Proveedor//////////////////////////////
    def formProve(self):
        #frame = tk.Frame(self.ventana1)
        vprove = tk.Toplevel(self.ventana1)
        vprove.title("Ingreso de Proveedores")
        vprove.config(bg="blue")
        mi_label = tk.Label(vprove,text="Por favor Ingrese los Datos").pack(anchor = 'center')
        
        frame=tk.Frame(vprove)
        
        frame.config(bg="blue")

        frame.pack()

        ##Formato formulario
        
        #mi_label.pack(side=tk.LEFT)
        #mi_label.config(font=("Arial",14))
        #mi_label.config(fg="blue")
        
        self.pro_codigo = tk.StringVar()
        self.pro_nombre = tk.StringVar()
        self.pro_direccion = tk.StringVar()
        self.pro_credito = tk.StringVar()


        cuadroID = tk.Entry(frame,textvariable=self.pro_codigo)
        cuadroID.grid(row=0,column=1,padx=10,pady = 10)

        cuadroNombre = tk.Entry(frame,textvariable=self.pro_nombre)
        cuadroNombre.grid(row=1,column=1,padx=10,pady = 10)

        cuadroDescripcion = tk.Entry(frame,textvariable=self.pro_direccion)
        cuadroDescripcion.grid(row=2,column=1,padx=10,pady = 10)

        cuadroTipo = tk.Entry(frame,textvariable=self.pro_credito)
        cuadroTipo.grid(row=3,column=1,padx=10,pady = 10)
        


        #etiquetas

        idLabel = tk.Label(frame,text="Código: ")
        idLabel.grid(row=0,column=0)
        nombresLabel = tk.Label(frame,text="Nombre: ")
        nombresLabel.grid(row=1,column=0)
        apellidosLabel = tk.Label(frame,text="Direccion: ")
        apellidosLabel.grid(row=2,column=0)
        cedulaLabel = tk.Label(frame,text="Credito: ")
        cedulaLabel.grid(row=3,column=0)
        
        #botones
        frame2 = tk.Frame(vprove)
        frame2.pack()
        botonCreate=tk.Button(frame2,text="Agregar",command=self.agregaProve)
        botonCreate.grid(row=0,column=0,padx=10,pady=10)

        botonRead=tk.Button(frame2,text="Consultar",command=self.consultarProve)
        botonRead.grid(row=0,column=1,padx=10,pady=10)

        botonUpdate=tk.Button(frame2,text="Actualizar",command=self.actualizarProve)
        botonUpdate.grid(row=0,column=2,padx=10,pady=10)

        botonDelete=tk.Button(frame2,text="Borrar",command=self.eliminarProve)
        botonDelete.grid(row=0,column=3,padx=10,pady=10)
    
    def agregaProve(self):
        conexion = sqlite3.connect('piezas.db')
        cursor = conexion.cursor()
        try:
            datos=self.pro_codigo.get(), self.pro_nombre.get(),self.pro_direccion.get(),self.pro_credito.get()
            cursor.execute("insert into proveedor values(? , ? , ? , ?)",datos)
        except sqlite3.IntegrityError:
            print("Registro  '{}' ya existe ".format(self.pro_codigo.get()))
        else:
            print("Registro '{}' creado correctamente".format(self.pro_codigo.get()))
            tk.messagebox.showinfo("Base de Datos", "Registro insertado con exito")
        conexion.commit()
        conexion.close()
    def consultarProve(self):
        conexion = sqlite3.connect("piezas.db")
        cursor = conexion.cursor()
        cursor.execute("Select * from proveedor where pro_codigo=" + self.pro_codigo.get())
        piezas = cursor.fetchall()
        if not piezas:
            print("Lista vacia")
            self.pro_codigo.set("")
            self.pro_nombre.set("")
            self.pro_direccion.set("")
            self.pro_credito.set("")
            tk.messagebox.showinfo("Base de Datos", "No existe ese registro...")
        for e in piezas:
            self.pro_codigo.set(e[0])
            self.pro_nombre.set(e[1])
            self.pro_direccion.set(e[2])
            self.pro_credito.set(e[3])
            
        conexion.commit()agregar_menu
        conexion.close()
    def actualizarProve(self):
        conexion = sqlite3.connect('piezas.db')
        cursor = conexion.cursor()
        
        
        datos=self.pro_nombre.get(),self.pro_direccion.get(),self.pro_credito.get()
        cursor.execute("update proveedor set pro_nombre=?, pro_direccion=? ,pro_credito=? "+"where pro_codigo="+ self.pro_codigo.get(),datos )
        
        tk.messagebox.showinfo("Base de Datos", "Registro actualizado con exito")
        conexion.commit()
        conexion.close()

    def eliminarProve(self):
        conexion = sqlite3.connect('piezas.db')
        cursor = conexion.cursor()
        cursor.execute("delete from proveedor where pro_codigo="+self.pro_codigo.get())
        tk.messagebox.showinfo("Base de Datos", "Registro eliminado con exito")
        conexion.commit()
        conexion.close()

   

###formulario inventario////////////////////////////////
    def formInv(self):
        #frame = tk.Frame(self.ventana1)
        vinv = tk.Toplevel(self.ventana1)
        vinv.title("Ingreso de Inventario")
        vinv.config(bg="blue")
        mi_label = tk.Label(vinv,text="Por favor Ingrese los Datos").pack(anchor = 'center')
        
        frame=tk.Frame(vinv)
        
        frame.config(bg="blue")

        frame.pack()

        ##Formato formulario
        
        #mi_label.pack(side=tk.LEFT)
        #mi_label.config(font=("Arial",14))
        #mi_label.config(fg="blue")
        
        self.sum_codigo = tk.StringVar()
        self.sum_precio = tk.DoubleVar()
        self.pie_codigo = tk.StringVar()
        self.pro_codigo = tk.StringVar()

        conexion = sqlite3.connect("piezas.db")
        cursor = conexion.cursor()
        cursor.execute("Select * from proveedor")
        prove = cursor.fetchall()
        cursor.execute("Select * from piezas")
        piez = cursor.fetchall()
        conexion.commit()
        conexion.close()
        ListProve = prove
        ListPiez = piez
        self.var = tk.StringVar(vinv)
        #var.set(ListProve[0])
        self.var.trace("w",partial(self.change,widget = self.var))
        
        cuadroID = tk.Entry(frame,textvariable=self.sum_codigo)
        cuadroID.grid(row=0,column=1,padx=10,pady = 10)
        
        listPr = tk.OptionMenu(frame,self.var , *ListProve)
        listPr.config(width=50, font=('Helvetica', 12))
        listPr.grid(row=1,column=1,padx=10,pady = 10)
        
       #########ListProve = prove
        self.var1 = tk.StringVar(vinv)
        #var1.set(ListPiez[0])
        self.var1.trace("w",partial(self.change1,widget = self.var1))

        listPz = tk.OptionMenu(frame,self.var1 , *ListPiez)
        listPz.config(width=50, font=('Helvetica', 12))
        listPz.grid(row=2,column=1,padx=10,pady = 10)

        # self.pie_codigo = var.get()
        # self.pro_codigo = var1.get()


        cuadroPrecio = tk.Entry(frame,textvariable=self.sum_precio)
        cuadroPrecio.grid(row=3,column=1,padx=10,pady = 10)

        #etiquetas
        idLabel = tk.Label(frame,text="Codigo: ")
        idLabel.grid(row=0,column=0)
        nombreLabel = tk.Label(frame,text="Proveedor: ")
        nombreLabel.grid(row=1,column=0)
        prodLabel = tk.Label(frame,text="Producto: ")
        prodLabel.grid(row=2,column=0)
        precLabel = tk.Label(frame,text="Precio: ")
        precLabel.grid(row=3,column=0)
       
        
        #botones
        frame2 = tk.Frame(vinv)
        frame2.pack()
        botonCreate=tk.Button(frame2,text="Agregar",command=self.agregaSumi)
        botonCreate.grid(row=0,column=0,padx=10,pady=10)

        botonRead=tk.Button(frame2,text="Consultar",command=self.consultarSumi)
        botonRead.grid(row=0,column=1,padx=10,pady=10)

        botonUpdate=tk.Button(frame2,text="Actualizar",command=self.actualizarSumi)
        botonUpdate.grid(row=0,column=2,padx=10,pady=10)

        botonDelete=tk.Button(frame2,text="Borrar",command=self.eliminarSumi)
        botonDelete.grid(row=0,column=3,padx=10,pady=10)
    def change(self,*args,widget=None):
        #self.pie_codigo=widget.get()[1]
        self.pie_codigo=self.var.get()[1]
        print("cange")
        print(widget.get()[1])

    def change1(self,*args,widget=None):    
        self.pro_codigo = self.var1.get()[1]
        print("cange1")
        print(widget.get()[1])

    def agregaSumi(self):
        print(self.pie_codigo[0])
        print(self.pro_codigo[0])
        conexion = sqlite3.connect('piezas.db')
        cursor = conexion.cursor()
        try:
            datos=self.sum_codigo.get(), self.sum_precio.get(), self.pie_codigo[0], self.pro_codigo[0]
            
            cursor.execute("insert into suministra values(? , ? , ? , ?)",datos)
        except sqlite3.IntegrityError:
            print("Registro  '{}' ya existe ".format(self.sum_codigo.get()))
        else:
            print("Registro '{}' creado correctamente".format(self.sum_codigo.get()))
            tk.messagebox.showinfo("Base de Datos", "Registro insertado con exito")
        conexion.commit()
        conexion.close()

    def consultarSumi(self):
        conexion = sqlite3.connect("piezas.db")
        cursor = conexion.cursor()
        cursor.execute("Select * from suministra where sum_codigo=" + self.sum_codigo.get())
        piezas = cursor.fetchall()
        if not piezas:
            print("Lista vacia")
            self.sum_codigo.set("")
            self.sum_precio.set("")
            tk.messagebox.showinfo("Base de Datos", "No existe ese registro...")
        for e in piezas:
            self.sum_codigo.set(e[0])
            self.sum_precio.set(e[1])
            #self.var1.set(e[2])
            #self.var.set(e[3])
        
        cursor.execute("Select * from piezas where pie_codigo=" + str(piezas[0][2]))
        pieza = cursor.fetchall()
        print(pieza)
        self.var1.set(pieza[0])
        cursor.execute("Select * from proveedor where pro_codigo=" + str(piezas[0][3]))
        pieza = cursor.fetchall()
        print(pieza)
        self.var.set(pieza[0])
        conexion.commit()
        conexion.close()


    def actualizarSumi(self):
        conexion = sqlite3.connect('piezas.db')
        cursor = conexion.cursor()
        
        datos=self.sum_precio.get(), self.pie_codigo[0], self.pro_codigo[0]
        
        cursor.execute("update suministra set sum_precio=?, pie_codigo=? ,pro_codigo=? "+"where sum_codigo="+ self.sum_codigo.get(),datos )
        
        tk.messagebox.showinfo("Base de Datos", "Registro actualizado con exito")
        conexion.commit()
        conexion.close()

    def eliminarSumi(self):
        conexion = sqlite3.connect('piezas.db')
        cursor = conexion.cursor()
        cursor.execute("delete from suministra where sum_codigo="+self.sum_codigo.get())
        tk.messagebox.showinfo("Base de Datos", "Registro eliminado con exito")
        conexion.commit()
        conexion.close()





    def Salir(self):
        respuesta = mb.askyesno("Salir","Esta seguro de salir del sistema")
        if respuesta == True:
            sys.exit()

    def crearBDD(self):
        conexion = sqlite3.connect("piezas.db")
        cursor = conexion.cursor()

        try :
            cursor.execute('''CREATE TABLE piezas(
                pie_codigo integer primary key autoincrement,
                pie_nombre varchar(15) not null,
                pie_descripcion varchar(25) not null,
                pie_tipo varchar(13) not null)
            ''')#se usa ''' para asegurar que sea cadena
        except sqlite3.OperationalError:
            print("La tabla ya existe")
        else:
            print("La tabla piezas se a creado satisfactoriamente")

        try :
            cursor.execute('''CREATE TABLE proveedor(
                pro_codigo integer primary key autoincrement,
                pro_nombre varchar(15) not null,
                pro_direccion varchar(25) not null,
                pro_credito char(1))
                
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
                pro_codigo integer not null,
                foreign key(pie_codigo) references piezas(pie_codigo),
                foreign key(pro_codigo) references proveedor(pro_codigo))
                
                
                    
                ''')#se usa ''' para asegurar que sea cadena
        except sqlite3.OperationalError:
            print("La tabla ya existe")
        else:
            print("La tabla siministra se a creado satisfactoriamente")
 
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
