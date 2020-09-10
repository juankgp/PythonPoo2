import getpass 
import sys
from busquedas import Validaciones, Correo , Mail
class Login:
    def __init__(self):
        print("********Bienvenido a su correo************")
        self.valida = Validaciones()
        self.correo = Mail()
        self.elecciones={
           "1":self.escribirCorreo,
           "2":self.listarCorreos,
           "3":self.buscarCorreo,
           "4":self.modificarReenviar,
           "5":self.eliminarCorreo,
           "6":self.quit
        }
    def run(self):    
        while True:
            self.usuario = self.valida.capturarCorreo("Ingrese su correo:")    # input("Ingrese su usuario:")
            self.clave = getpass.getpass(prompt='Ingrese su contraseña: ')
            if(self.valida.valida(self.usuario,self.clave)):
                while True:
                    self.mostrarMenu()
                    eleccion = input("Escoja una opción: ")
                    accion = self.elecciones.get(eleccion)
                    if accion:
                        accion()
                    else:
                        print("{0} no es una eleccion valida". format(eleccion))#{0} valor por default toma el valor no correcto
            else:
                print("¡¡¡¡¡¡¡¡¡Credenciales incorrectas vuleva a intentar.!!!!!!!!!!!")

    def quit(self):
        print("Gracias por usar CorreoJK")
        sys.exit(0)
    def eliminarCorreo(self):
        print("¡¡¡¡¡¡¡¡¡¡¡¡¡Lista de Correo!!!!!!!!!!!!!")
        self.listarCorreos()
        id = input("Ingrese el nuero de correo a Eliminar")
        self.correo.borrarCorreo(id)
    def modificarReenviar(self):
        id = input("Ingrese el nuero de correo a modificar")
        asunto = input("Ingrese el nueo asunto: ")
        correo = input("Ingrese el nuevo correo: ")
        if asunto:
            self.correo.modificarAsunto(id,asunto)
        if correo:
            self.correo.modificarCorreo(id,correo)
        print("-------------Correo reenviado-------------")

    def listarCorreos(self, correos = None):
        print("-------------Listando correos-----------------")
        if not correos:
            correos = self.correo.correos
        for p in correos:
            print("{0} \t {1} \t {2} \t {3} \t{4} ".format(p.id,p.destinatario,p.asunto,p.correo,p.fechaEnvio))
        input("Listas.................")

    def buscarCorreo(self):
        #self.listarCorreos()
        filter = input("Buscar por: ")
        bcorreo = self.correo.buscar(filter)
        self.listarCorreos(bcorreo)

    def escribirCorreo(self):
        print("##########Redaccion de Correo############")
        destino = self.valida.capturarCorreo("Ingrese el correo del destinatario: ")
        asunto = input("Ingrese el asunto: ")
        cuerpo = input("Ingrese el correo: ")
        self.correo.nuevoCorreo(destino,asunto,cuerpo)
        input("Correo enviado.................")

    def mostrarMenu(self):
         print("""Menu Opciones
            1. Escribir Correo
            2. Listar Correos
            3. Buscar Correo
            4. Modificar y reenviar
            5. Borrar Mail
            6. Salir""")




if __name__ == "__main__":
    Login().run()