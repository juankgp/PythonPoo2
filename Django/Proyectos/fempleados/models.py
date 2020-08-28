from django.db import models

# Create your models here.
class Empleados(models.Model):
    Apellido = models.CharField(max_length=25)
    Nombres = models.CharField( max_length=25)
    Cedula = models.CharField(max_length=14)
    FechaNacimiento = models.DateField()
    
    def NombreCompleto(self):
        cadena = "{0} {1}, {2}"
        return cadena.format(self.Apellido, self.Nombres)

        def __str__(self):
            NombreCompleto = "{0},{1}"
            return self.NombreCompleto()


class Prestamos(models.Model):
    fecha = models.DateField()
    valor = models.DecimalField(max_digits=3, decimal_places=2)
    plazo = models.CharField(max_length=25)
    estado = models.BooleanField(default = False)
                
    def __str__(self):
        return "{0} {1}".format(self.valor, self.plazo)

class Departamentos(models.Model):
    nombreDep = models.CharField(max_length=25)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return "{0} ({1})".format(self.nombreDep,self.estado)
    