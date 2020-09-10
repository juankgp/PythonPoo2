#herencia simple

class Estudiante():
    def __init__(self,edad,nombre):
        self.edad = edad
        self.nombre = nombre

class Desarrollo(Estudiante):
    def presentacion(self):
        print(f"Hola soy {self.nombre}")
        print(f"Mi edad es {self.edad}")

#referencia a calase estudiante
estudiante = Estudiante(23,"Juank Gutierrez")
print(f"Nombre: {estudiante.nombre}")
print(f"Edad: {estudiante.edad}")
#referencia a la clase desarrollo

estudiante = Desarrollo(26,"Jose Pepe")
estudiante.presentacion()