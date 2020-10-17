
class Empleado():

    def __init__(self,ci,nombre,edad):
        self._ci=ci
        self._nombre=nombre
        self._edad=edad


    @property
    def ci(self):
        return self._ci
    
    @ci.setter
    def ci(self,ci):
        self._ci=ci
    
    @property
    def nombre (self):
        return self._nombre
    
    @nombre.setter
    def nombre(self,nombre):
        self._nombre=nombre
    
   
    @property
    def edad(self):
        return self._edad

       
    @edad.setter
    def edad(self,edad):
        if edad > 0:
            self._edad=edad
        else:
            raise ValueError("Edad Incorrecta") # Exception Control de un error
     
    
    