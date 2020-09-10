#atributos y metodos
#Tiene la capacidad de definor variables y funciones dentro de las clases

class Galleta:
    pass


galleta = Galleta()
galleta.sabor = "dulce"
galleta.color = "tomate"

print(f'El sabor de galleta es: {galleta.sabor}')
print(f'El color de la galleta es: {galleta.color}')

#atributos en la clase
print("-----------------")
class GalletaA:
    chocolate=False

GalletaA.chocolate=True
galletaa = GalletaA()
#galletaa.chocolate = True
#utilizo el atributo declarado en la clase
if galletaa.chocolate:
    print("La galleta es de chocolate")

else:
    print("La galleta no es de chocolate")

#metodos
print("----------------------")
class GalletaM:
    chocolate = False
    def saludar(self): #referenciamos a la clase con self
        self.chocolate = True

galletam = GalletaM()

galletam.saludar()
print(galletam.chocolate)

#metodos especiales
#cosntructores: es un metodo que se llama automaticamente al crear un objeto __init

class GalletaC:
    def __init__(self):
        print("Galleta muy dulce")

galletac = GalletaC()
print(galletac.__class__.__name__)
