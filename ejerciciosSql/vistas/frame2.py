from tkinter import *



root=Tk()
root.title("Binevenidos")
root.resizable(1,1)

frame = Frame(root,width=180,height=120)
frame.pack()
##frame.config(cursor = "arrow")
frame.config(cursor = "pirate")
frame.config(bg = 'lightblue')
root.config(cursor = "pirate")
root.config(bg = 'blue')
root.mainloop()