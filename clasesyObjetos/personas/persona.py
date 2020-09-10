class Persona():
    def __init__(self,ci,nombre,edad):
        self._ci=ci
        self._nombre=nombre
        self._edad=edad

    @property
    def pci(self):
        return self._ci
    @pci.setter
    def pci(self,ci):
        self._ci=ci

    @property
    def pnombre(self):
        return self._nombre
    @pnombre.setter
    def pnombre(self,nombre):
        self._nombre=nombre

    @property
    def pedad(self):
        return self._edad

    @pedad.setter
    def pedad(self,edad):
        if edad > 0:
            self._edad=edad
        else:
            raise ValueError("Edad incorrecta")#exception

    def __str__(self):
        return self._ci.__str__() + " " + self.pnombre + " (" + str(self.pedad)+")"