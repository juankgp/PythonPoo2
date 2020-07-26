
class Casa():


    def __init__(self, precio):
        self._precio = precio

 
    @property
    def precio(self):
        return self._precio
    
    @precio.setter
    def precio(self, nuevo_precio):
        if nuevo_precio > 0 and isinstance(nuevo_precio, float):
            self._precio = nuevo_precio
        else:
            print("Ingrese el precio valido.")

    @precio.deleter
    def precio(self):
        print("Borrando precio")
        del self._precio


casa = Casa(25000)

print(casa.precio)
del casa.precio

casa.precio=24000.0

print(casa.precio)
