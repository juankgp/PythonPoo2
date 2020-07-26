def capturarEntero(mensaje):
    while True:
        try:
            numero=int(input(f'{mensaje}:'))
            return numero
        except ValueError:
            print('****************** Error debe digitar un numero entero ******************')
        print()
def capturarNota(mensaje):
    while True:
        try:
            numero=float(input(f'{mensaje}:'))
            if numero<0 or numero>10:
                print('Nota Invalido')
                continue
            return numero
        except ValueError:
            print('****************** Error debe digitar una nota valida ******************')
        print()
def capturarFloat(mensaje):
    while True:
        try:
            numero=float(input(f'{mensaje}:'))
            return numero
        except ValueError:
            print('****************** Error debe digitar una nota valida ******************')
        print()
def capturarCorreo(mensaje):
    haya = False
    hayp = False
    while True:
        correo = input(f"{mensaje}")
        for p in correo:
            if p == "@":
                haya = True
            if p == ".":
                hayp = True
        if haya == True and hayp == True:
            return correo
        else:
            print("-------------Correo incorrecto vuelva a intentar-----------------a")
def capturarCadena(mensaje):
    while True:
        try:
            cadena=str(input(f'{mensaje}:')).strip()
            if not cadena:
                print('Dato invalido')
                continue
            return cadena
        except ValueError:
            print('****************** Error debe digitar una cadena ******************')
        print()
        
class Estudiante:
    def __init__(self):
        self.nombre = capturarCadena("Ingrese los nombres: ")
        self.apellidos = capturarCadena("Ingrese los Apellidos: ")
        self.edad = capturarEntero("Ingrese la edad del Estudiante")
        self.sexo = capturarCadena("Ingrese el sexo: ")
        self.direccion = capturarCadena("Ingrese la direccion: ")
        self.telefono = capturarCadena("ingrese el telefono: ")
        self.email = capturarCorreo("Ingrese el correo Electronico: ")
    def datos(self):
        print(f"Los nombres del estudiante son: {self.nombre}")
        print(f"Los apellidos del estudiate son: {self.apellidos}")
        print(f"La edad del estudiante es: {self.edad}")
        print(f"El sexo del estudainte es: {self.sexo}")
        print(f"La direccion del estudiante es: {self.direccion}")
        print(f"El telefono del estudiante es: {self.telefono}")
        print(f"El email del estudiante es: {self.email}")
        print("-------------------------------")
    def ingNotas(self,lcalif):
        for i in range(5):
            lcalif.append(capturarNota(f"Ingrese la nota {i+1} del estudinate"))       
        return lcalif

    def notas(self,notas):
        promedio = 0
        for p in notas:
            promedio = promedio + p
        promedio = promedio / 5
        if promedio >= 7:
            print("Aprueba la materia")
        else:
            print("No aprueba la materia")
        return promedio

class saldoCEstudiante:
    def __init__(self):
        self.saldo = capturarFloat("Ingrese su saldo de la cuenta")

    def debito(self,cantidad):
        if cantidad <= self.saldo:
            self.saldo = self.saldo - cantidad
            print("Transaccion Exitosa")
            print(f"Su nuevo saldo es: {self.saldo}")
        else:
            print("Transaccion rechazada")


calif = []
estudiante = Estudiante()
estudiante.datos()
 
calif = estudiante.ingNotas(calif)
promedio = estudiante.notas(calif)

print(f"con un promedio de {promedio}")

saldo = saldoCEstudiante()
pension = capturarFloat("Ingrese el valor de la pension")
saldo.debito(pension)