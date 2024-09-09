from django.db import models

# Create your models here.
class Trabajador(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    sexo = models.CharField(max_length=1, null=True, blank=True)
    experiencia = models.IntegerField()
    
    def __str__(self):
        return f"Trabajador {self.id} - Nombre: {self.nombre}"
