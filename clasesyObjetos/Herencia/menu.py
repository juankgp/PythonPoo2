import sys
from cuaderno import Cuaderno , Nota

class Menu:
    def __init__(self):
        self.cuaderno = Cuaderno()
        self.elecciones={
            "1":self.mostrar_notas,
            "2":self.buscar_notas,
            "3":self.agregar_nota,
            "4":self.modificar_nota,
            "5":self.quit
        }
    def mostrar_menu(self):
        print("""Menu Cuaderno
            1. Mostrar todas las Notas
            2. Buscar Notas
            3. Añadir Nota
            4. Modificar Nota
            5. Salir""")

    def run(self):
        #MOstar el menu y seleccion de la opcion}
        while True:
            print("----------------------------------")
            self.mostrar_menu()
            eleccion = input("Escriba una opcion: ")
            accion = self.elecciones.get(eleccion)
            if accion:
                accion()
            else:
                print("{0} no es una eleccion valida". format(eleccion))#{0} valor por default toma el valor no correcto

    def agregar_nota(self):
        memo = input("Escriba un memo o nota: ") 
        #tag = input("Escriba una tag")
        self.cuaderno.nueva_nota(memo)
        print("Nota agregada")

    def mostrar_notas(self,notas = None):
        if not notas:
            notas = self.cuaderno.notas
        for nota in notas:
            print("{0}:{1} \n {2}".format(nota.id , nota.tags , nota.memo))
    def buscar_notas(self):
        filter = input("Buscar por: ")
        notas = self.cuaderno.buscar(filter)
        self.mostrar_notas(notas)

    def modificar_nota(self):
        id = input("Escriba el id de la nota a modif")
        memo = input("esciba el memo")
        tags = input("Escriba el tag")
        if memo:
            self.cuaderno.modificar_memo(id,memo)
        if tags:
            self.cuaderno.modificar_tags(id,tags) 

    def quit(self):
        print("Gracias por usar")
        sys.exit(0)

if __name__ == "__main__":
    Menu().run()