from tkinter import *
#from tkinter import messagebox as Messagebox

ventana = Tk()
frame = Frame(ventana)
label =Label(frame,text="")
label.pack()#inicia paquete label
ventana.geometry('450x400')
ventana.title('Labels')
Label(ventana,text = 'Desarrollo de Software').pack(anchor = CENTER)
img = PhotoImage(file = "botonInicio.png")
Label(ventana,image =img).pack(side = "left")

ventana.mainloop()
