class Cancion:
    def __init__(self,autor,titulo,duracion):#duracion en segundos
        self.duracion=duracion
        self.titulo=titulo
        self.duracion=duracion
    def __len__(self):
        return f"Duracion: {self.duracion} Titulo: {self.titulo}"

cancion = Cancion("Arjona","Mujeres","120")
print(cancion.__len__())
