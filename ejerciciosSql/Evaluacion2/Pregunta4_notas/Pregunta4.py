

#Pregunta 4.
##########################################################
'''
Creat una tabla llamada record_estudiante cuyos campos son:
rec_codigo, rec_nombres, rec_apellidos, rec_nacademica, rec_ntesis, rec_npromedio, rec_indicador
Considere mensajes messagebox para notificar si la tabla ha sido creada

'''
##########################################################
#Pregunta 5
'''
Mediante Tkinter el sistema debe crear un menú para insertar y consultar información del record Acádemico
Cree botones para hacer el llamado a la ventana
De estilo a las tablas
'''

##########################################################
import tkinter as tk
from tkinter import messagebox as mb
import sys
import sqlite3


class Instituto:
    def __init__(self):
        
        
        self.ventana1=tk.Tk()
        self.ventana1.geometry("600x550")
        self.ventana1.title("Sistema de Notas")
               
        
        imagen = tk.PhotoImage(file="ismac.png")
        tk.Label(master=self.ventana1, image=imagen, bd=0, width=300, height=300).pack(side="top")

        self.agregar_menu()
        self.ventana1.mainloop()
    

    def agregar_menu(self):
        self.menubar1 = tk.Menu(self.ventana1)
        self.ventana1.config(menu=self.menubar1)
        self.archivo = tk.Menu(self.menubar1, tearoff=0)
        ####################SubMenus###################################################
        ###########Opciones###############
        self.archivo.add_command(label="Crear base de Datos",command=self.crearBdd)
        self.archivo.add_command(label="Salir",command=self.Salir)
        ################################# Menus ###############################3
        self.menubar1.add_cascade(label="Archivo",menu=self.archivo)#creo el menu archivo
       
    def crearBdd(self):
        conexion=sqlite3.connect("record_estudiante.db")
        cursor=conexion.cursor()
        #Creo la tabla empleado
        try:
            cursor.execute('''CREATE TABLE record(
                rec_codigo integer primary key autoincrement,
                rec_nombres varchar(15) not null,
                rec_apellidos varchar(15) not null,
                rec_nacademica int not null,
                rec_ntesis varchar(15) not null,
                rec_npromedio float not null,
                rec_indicador varchar(2) not null)
                ''')

        except sqlite3.OperationalError:
            tk.messagebox.showerror("Error","La Tabla empleado ya existe")
            
        else:
            tk.messagebox.showinfo("BDD","La Tabla empleado se creo con exito")  

        try:
            cursor.execute('''CREATE TABLE usuario(
                rec_codigo integer primary key autoincrement,
                rec_user varchar(15) not null,
                rec_password varchar(15) not null)
                ''')

        except sqlite3.OperationalError:
            tk.messagebox.showerror("Error","La Tabla usuario ya existe")
            
        else:
            tk.messagebox.showinfo("BDD","La Tabla usuario se creo con exito")  

    def Salir(self):
        respuesta = mb.askyesno("Salir","Esta seguro de salir del sistema")
        if respuesta == True:
            sys.exit()

vinstituto=Instituto() 