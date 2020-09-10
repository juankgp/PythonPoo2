from tkinter import *
from tkinter import messagebox as Messagebox

def test():
    Messagebox.askyesnocancel("Bienvenidos","Tercero de desarrollo")


root=Tk()
frame = Frame(root,width=480,height=300)

frame.pack()

frame.config(bg = 'lightblue')


Button(frame,text = 'Clic' , command = test).pack()

root.mainloop()