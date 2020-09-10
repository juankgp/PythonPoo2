class Mascotas(object):
    def __init__(self,nombre,raza):
        self.nombre=nombre
        self.raza=raza

    def __str__(self):
        return f"{self.nombre} es de raza {self.raza}"

vmascota = Mascotas("Firulais","Golden")
print(str(vmascota))