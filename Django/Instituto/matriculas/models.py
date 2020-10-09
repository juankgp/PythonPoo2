from django.db import models

# Create your models here.
class Matriculas(models.Model):
        Estudiante=models.CharField(max_length=25)
        Carrera=models.CharField(max_length=25)
        Semestre=models.CharField(max_length=14)
        Fecha=models.DateField()
        Costo=models.PositiveIntegerField(default=0)
        NotaSemAnt = models.PositiveIntegerField(default=0)
        Paralelo = models.CharField(max_length=5,default="A")
        

        def __str__(self):
            return "{0} ({1})".format(self.Estudiante,self.Carrera)