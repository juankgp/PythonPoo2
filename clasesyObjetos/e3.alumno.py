class Alumno:
    def __init__(self):
        self.nombre=input("Ingrese el nombre del Alumno")
        self.nota = input("Ingrese la nota final")

    def imprimir(self):
        print(f"Alumno: {self.nombre}")
        print(f"Nota: {self.nota}")

    def validador(self):
        if int(self.nota) > 7:
            print(f"{self.nombre} a Aprobado")
        else:
            print(f"{self.nombre} a Reprobado")


alumno = Alumno()
alumno.imprimir()
alumno.validador()
alumno2 = Alumno()
alumno2.imprimir()
alumno2.validador()