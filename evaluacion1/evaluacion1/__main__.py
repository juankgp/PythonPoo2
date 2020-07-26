from .inventario_funciones import registrarAlumno, mostrarResultadoFact,mostrarMaterias,registrarMateria
from .tupla import printMaterias
def mostrar_menu():

    print('1. Determinar el costo de matrícula')
    print('2. Registar materias ')
    print('3. Valido Opción')
    print('4. Pasos para crear Ambientes virtuales')
    print('0. Salir')

def capturarCadena(mensaje):
    while True:
        try:
            cadena=str(input(f'{mensaje}:'))
            return cadena
        except ValueError:
            print('Error debe digitar una cadena no vacia:')
        print()

def capturarFloat(mensaje):
    while True:
        try:
            numero=float(input(f'{mensaje}:'))
            return numero
        except ValueError:
            print('Error debe digitar un numero entero:')
        print()

def capturarEntero(mensaje):
    while True:
        try:
            numero=int(input(f'{mensaje}:'))
            return numero
        except ValueError:
            print('Error debe digitar un numero entero:')
        print()


def main():
    while True: 
        try:
            mostrar_menu()
            opcion =int(input('Digite la opción: '))
            if 0 <= opcion <= 5:
                break
            else: 
                print ('La opción debe estar entre 1 y 5')
        except ValueError:
                    print()
                    print('Error: Debe digitar un numero entero valido')

    if opcion == 1:
            alumnos = []
            print("Opcion 1")
            nombres=capturarCadena('Ingrese los nombres para la factura : ')
            cedula = capturarCadena('Ingrese la cedula')   
            costo = capturarFloat('Ingrese el valor de matricula')
            descuento = capturarEntero('Ingrese el descuento')
            nuevoAlumno = {'nombres':nombres , 'cedula':cedula , 'costo':costo , 'descuento':descuento}
           
            registrarAlumno(alumnos,nuevoAlumno)
            print()
            mostrarResultadoFact(nuevoAlumno)

    if opcion == 2: 
        print("Opcion 2")
        materias =[]
        numMat = 1
        while True:
            nombresMaterias=capturarCadena(f'Ingrese la materia N {numMat}')
            numMat = numMat+1
            nuevaMateria = {'nombre':nombresMaterias}
            registrarMateria = (materias,nuevaMateria)
            mostrarMaterias(nuevaMateria)
            if numMat > 5:
                break

    if opcion == 3:
        
        print("Opcion 3")
        printMaterias()
    if opcion == 4:
        print('Pasos para crear ambientes virtuales')
        print('Ubicarse en la carpeta donde se quiere crear el ambinete virtual')
        print('1.- Correr el comando pip install pipenv')
        print('2.- De ser el caso actualizar la version de pip con el comado: python -m pip install --upgrade pip ')
        print('3.- Correr el comando pip install pipenv')
        print('4.- Crear el ambienrte virtual con: pipenv install request')
        print('Ingreso a verificar si el entorno vistual esta funcionando con : pipenv shell')
        print('Ejecutar pip freeze para los requerimientos python –m pip freeze')
        print('Ejecutar el modulo instalado con python')


        
if __name__ == '__main__':
    main()