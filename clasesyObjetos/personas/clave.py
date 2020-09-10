import getpass
class Empleado:
    def __init__(self):
        self.usuario = input("Ingrese su usuario: ")
        self.__clave = getpass.getpass("Ingrse su contraseña: ")

    

    @property
    def key(self):
        return self.__clave
    @key.setter
    def key(self,newClave):
        self.__clave = newClave


#empleado = Empleado()
#print(empleado.getClave)
#empleado.key = getpass.getpass("Ingrese la nueva clave: ")
#print(empleado.key)


