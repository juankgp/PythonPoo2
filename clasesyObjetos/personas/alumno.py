from persona import Persona  #from (nombre archivo) import (Clase)

class Alumno(Persona):
    def __init__(self,ci,nombre,edad,profesion):
        Persona.__init__(self,ci,nombre,edad)
        self.profesion = profesion
   # def __str__(self):
    #    return Persona.__str__(self)

    def __str__(self):
        return Persona.__str__(self) + self.profesion

alumno = Alumno("1714574801", "Juank" , 36,"Est")
print(alumno.__str__())