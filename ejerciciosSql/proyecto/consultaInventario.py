import sqlite3
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont



class Table(tk.Frame):
    def __init__(self, parent=None, title="", headers=[], height=10):
        tk.Frame.__init__(self, parent)
        self._title = tk.Label(self, text=title, background="#ECCCCE", font=("Helvetica", 16))
        self._headers = headers
        self._tree = ttk.Treeview(self,
                                  height=height,
                                  columns=self._headers, 
                                  show="headings")
        self._title.pack(side=tk.TOP, fill="x")

 

        # Agregamos dos scrollbars 
        vsb = ttk.Scrollbar(self, orient="vertical", command=self._tree.yview)   # horientacion vertical
        vsb.pack(side='right', fill='y')
        hsb = ttk.Scrollbar(self, orient="horizontal", command=self._tree.xview)  # horientacion horizontal
        hsb.pack(side='bottom', fill='x')

 

        self._tree.configure(xscrollcommand=hsb.set, yscrollcommand=vsb.set)
        self._tree.pack(side="left")

 

        for header in self._headers:
            self._tree.heading(header, text=header.title())
            self._tree.column(header, stretch=True,
                              width=tkFont.Font().measure(header.title()))
            

 

    def add_row(self, row):
        self._tree.insert('', 'end', values=row)
        for i, item in enumerate(row):
            col_width = tkFont.Font().measure(item)
            if self._tree.column(self._headers[i], width=None) < col_width:
                    self._tree.column(self._headers[i], width=col_width)
    
def ventanaInventario(parent=None):
    coninv=tk.Toplevel(parent,bg='#E8C8CD')
    coninv.title("Consulta de Proveedores")
    coninv.geometry('400x300')
    coninv.configure(bg="#444455")
    invHeaders=("Código","Precio"," Codigo Pieza","Codigo Proveedor")
    invTab=Table(coninv,title="Inventarios",headers=invHeaders)
    invTab.pack()
    
    conexion=sqlite3.connect("piezas.db")
    cursor=conexion.cursor()
    cursor.execute("Select sum_codigo, sum_precio from suministra")
    pieza = cursor.fetchall()
  
    
 
    #cursor2=conexion.cursor()
    
    cursor=conexion.cursor()
    cursor.execute("Select sum_codigo, sum_precio, pie_codigo , pro_codigo from suministra")
    print(str(pieza[0][0]))
   
    for row in cursor:
        print(row)
        # cursor1=conexion.cursor()
        # cursor1.execute("Select pie_nombre from piezas where pie_codigo =" + str(row[2]))
        # parte = cursor1.fetchall()
        # print(parte)
       # for nrow in cursor1:
       #     row = row + nrow
        invTab.add_row(row)
        

# ventana=tk.Tk()
# ventanaReporte(parent=ventana)
# ventana.mainloop()