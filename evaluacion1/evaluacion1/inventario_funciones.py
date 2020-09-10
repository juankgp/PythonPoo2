from datetime import datetime
from collections import Counter

def registrarAlumno(lAlumnos,alumno):
    lAlumnos.append(alumno)
    #print(productos)


def registrarMateria(materias,materia):
    materias.append(materia)
    #print(productos)

def mostrarResultadoFact(alumno):
    print()
    print(f"Nombres: {alumno['nombres']}")
    print(f'Cedula: {alumno["cedula"]}')
    print(f'costo: {alumno["costo"]}')
    print(f'descuento: {alumno["descuento"]}')
    print(f'El total es:{alumno["costo"]-(alumno["costo"]*alumno["descuento"]/100)}')
    
def mostrarMaterias(materia):
    print()
    print(f"Nombre materia: {materia['nombre']}")
    