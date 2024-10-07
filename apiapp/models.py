from django.db import models

# Create your models here.
class Trabajador(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    experiencia = models.IntegerField()
    
    def __str__(self):
        return f"Trabajador {self.id} - Nombre: {self.nombre}"
    
    
class Expediente(models.Model):
    id = models.IntegerField(primary_key=True)
    trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE, related_name='expedientes')
    sexo = models.CharField(max_length=1)
    edad = models.IntegerField(default=18)
    lugar_accidente = models.TextField(null=True, blank=True)
    fecha_suceso = models.CharField(max_length=16, null=True)
    lesion = models.TextField(null=True, blank=True)
    descripcion_hechos = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"Expediente de {self.trabajador.id}"
    
    
class Imagenes(models.Model):
    expediente = models.ForeignKey(Expediente, on_delete=models.CASCADE, related_name='imagen')
    imagen = models.ImageField(upload_to='imagenes/')
    
