import tkinter as tk
from tkinter import messagebox as mb
import sqlite3


class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk
        #self.ventana1.geometry("600x500")
        self.ventana1.title("Sistema de Prestamos")

        self.ventana1.mainloop()
aplicacion1 = Aplicacion()
