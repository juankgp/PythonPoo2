from django.db import models

# Create your models here.
class Piezas(models.Model):
    Nombre = models.CharField(max_length=15)
    Descripcion = models.CharField( max_length=25)
    Tipo = models.CharField(max_length=13)
    def __str__(self):
        return "{0} {1}".format(self.Nombre, self.Descripcion)
    # def NombreCompleto(self):
    #     cadena = "{0} {1}, {2}"
    #     return cadena.format(self.Apellido, self.Nombres)

    #     def __str__(self):
    #         NombreCompleto = "{0},{1}"
    #         return self.NombreCompleto()


class Proveedor(models.Model):
    #valor = 
    Nombre = models.CharField(max_length=15)
    Direccion = models.CharField(max_length=25)
    Credito = models.BooleanField(default=False)
                
    def __str__(self):
        return "{0} {1}".format(self.Nombre, self.Direccion)

class Suministra(models.Model):
    Precio = models.DecimalField(max_digits=3, decimal_places=2)
    Pieza_cod = models.ForeignKey(Piezas,on_delete=models.CASCADE)
    Proveedor_cod = models.ForeignKey(Proveedor,on_delete=models.CASCADE)

    def __str__(self):
        return "{0} {1}".format(self.Precio,self.Pieza_cod)