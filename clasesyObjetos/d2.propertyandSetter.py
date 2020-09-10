import getpass 
def impresion():
    print("-----------------------------")
    print(f"Nombres: {empleado.pNombres}")
    print(f"Usuario: {empleado.pUserName}")
    print(f"Clave: {empleado.pClave}")  
    print(f"Email: {empleado.pEmail}")
print("-----------------------------")

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
class Empleado():
    def __init__(self):
        self.__nombres = input("Ingrese los nombres: ")
        self.__userName = input("Ingrese el nombre de usuario: ")
        self.__clave = getpass.getpass(prompt="Ingrese su clave: ")
        self.__email = capturarCorreo("Ingrese su correo: ")
    @property
    def pNombres(self):
        return self.__nombres
    @property
    def pUserName(self):
        return self.__userName
    @property
    def pClave(self):
        return self.__clave
    @property
    def pEmail(self):
        return self.__email
    @pClave.setter
    def pClave(self,newPass):
        self.__clave = newPass
        print("Contraseña Cambiada")

    @pEmail.setter
    def pEmail(self,newEmail):
        self.__email = newEmail 

empleado = Empleado()
impresion()
empleado.pClave = getpass.getpass(prompt="Ingrese su nueva clave: ")
pos = empleado.pEmail.find("@")
empleado.pEmail = empleado.pEmail[pos:]
empleado.pEmail = empleado.pUserName + empleado.pEmail
print(empleado.pEmail)
