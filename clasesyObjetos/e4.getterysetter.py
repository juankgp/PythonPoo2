#getter @property se encarga de interceptar la lectura de un atributo get-obtener
# , setter se encargara de interceptar cuando se escriba set=definir
#Deleter se encarga de eliminar el contenido enviado

class Perros(object):
    def __init__(self, nombre, peso):
        self.__nombre = nombre
        self.__peso = peso

    @property
    def nombreG(self):#metodo para obtener el nombre
        return self.__nombre

    @nombreG.setter
    def nombreG(self,newName):
        print("Modificando el nombre....")
        self.__nombre = newName
        print(f"El nuevo nombre es :{self.__nombre}")

    @nombreG.deleter
    def nombreG(self):
        print("Borrando el nombre")
        del self.__nombre

iperro = Perros("Firulais",27)
print(iperro.nombreG)
iperro.nombreG = "Perro"
print(iperro.nombreG)
del iperro.nombreG

