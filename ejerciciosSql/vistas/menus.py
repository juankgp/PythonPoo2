from tkinter import *

def doNothing():
    temp = Toplevel(ventana)
    boton = Button(temp,text = "")
    boton.pack()

ventana = Tk()

menuBar = Menu(ventana)###toda la barra de menus
ventana.title("Mi proyecto")
fileMenu = Menu(menuBar , tearoff = 0)
fileMenu.add_command(label = "Nuevo" , command = doNothing)
fileMenu.add_command(label = "Abrir" , command = doNothing)
fileMenu.add_separator()#separa entre menus
fileMenu.add_command(label = "Salir" , command = doNothing)
menuBar.add_cascade(label = "Archivo",menu=fileMenu) #referencia a los menus


#menuEdit = Menu(ventana)
editMenu = Menu(menuBar , tearoff = 0)
editMenu.add_command(label = "Copiar" , command = doNothing)
editMenu.add_separator()#separa entre menus
editMenu.add_command(label = "Pegar" , command = doNothing)
editMenu.add_command(label="Cortar" , command=doNothing)
editMenu.add_command(label="Buscar" , command=doNothing)
menuBar.add_cascade(label = "Editar",menu=editMenu) #referencia a los menus

ventana.config(menu=menuBar)


ventana.mainloop()