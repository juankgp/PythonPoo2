#Clases y objetos

numero = 10
print("Numero es de tipo ",type(numero))

def hola():
    pass

print("def es de tipo", type(hola))

#definicion de una clase
#sintaxis
#class nombre:
#   pass

class Galleta:
    pass

#instanciacion de una clase
print("----------------------")
unaGalleta = Galleta()
otraGalleta = Galleta()
print(unaGalleta) #impreimo un objeto
print(otraGalleta) #imprimo otro objeto
print(Galleta)
#como consultar la clase de un objeto por medio de: __class
print("---------------------------")
print(type(unaGalleta))#a que clase pertenece el objeto unaGalleta
print(otraGalleta.__class__)#a que clase pertenece el objeto otraGalleta
print("---------------------------")
print(type(unaGalleta).__name__)
print(unaGalleta.__class__.__name__)
