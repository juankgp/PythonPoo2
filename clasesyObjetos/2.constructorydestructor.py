#metodos especiales
#cosntructores: es un metodo que se llama automaticamente al crear un objeto __init
class Galleta:
    chocolate = False
    def __init__(self,sabor,color):#constructor
        self.sabor = sabor
        self.color = color
        print(f"Se acaba de crear una galleta {self.sabor} y de color {self.color}")

galleta1 = Galleta("salada","marron")
galleta2 = Galleta("Muy Dulce","Blanca")


#destructor
class GalletaD:
    def __del__(self):
        print("La galleta a sido eliminado")
galletad = GalletaD()
galletad.__del__()
del(galletad)