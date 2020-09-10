#es el metodo (str)
#devuelve la representaion de un objeto en forma de cadena
#cambia el comportamiento de un objeto

class Galleta:
    def __init__(self,sabor,color):
        self.sabor = sabor
        self.color=color
     
    def __str__(self):
        return f"la galleta es de color {self.color} y de sabor {self.sabor}"
        
galletastr=Galleta("dulce","blanca")
#los tres siguinetes es lo mismo
print(galletastr)#imprimo los valores de una clase
print(str(galletastr))#imprimo los valores de la clase con metodo str
print(galletastr.__str__())