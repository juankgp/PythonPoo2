class Empleado:
    def __init__(self,nombres,apellidos,anionac):
        self.nombres=nombres
        self.__apellidos=apellidos
        self.__anionac=anionac
    
    @property
    def apellidosP(self):#metodo para obtener el nombre
        return self.__apellidos

    @property
    def anionacP(self):#metodo para obtener el nombre
        return self.__anionac

    @anionacP.setter
    def anionacP(self,anioact):
        self.__anionac = anioact - self.__anionac
        print(f"la edad es :{self.__anionac}")

name = input("Ingrese el nombre")
apell = input("Inhgrese el apellido")
anio = int(input("Ingrese la edad"))

empleado =Empleado(name,apell,anio)

print(f"Datos del empleado nombre: {empleado.nombres} apelidos: {empleado.apellidosP} y anio nacimiento {empleado.anionacP}")

print(f"la edad es: {2020-empleado.anionacP}")
empleado.anionacP=2020