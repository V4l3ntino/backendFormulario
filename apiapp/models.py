from django.db import models

# Create your models here.
class Trabajador(models.Model):
    id = models.CharField(primary_key=True, max_length=12)
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    experiencia = models.IntegerField()
    
    def __str__(self):
        return f"Trabajador {self.id} - Nombre: {self.nombre}"
    
    
class Expediente(models.Model):
    id = models.CharField(primary_key=True, max_length=37)
    trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE, related_name='expedientes')
    sexo = models.CharField(max_length=1)
    edad = models.IntegerField(default=18)
    puesto_trabajo = models.TextField(null=True, blank=True)
    lugar_accidente = models.TextField(null=True, blank=True)
    fecha_suceso = models.CharField(max_length=16, null=True)
    lesion = models.TextField(null=True, blank=True)
    lesionado_check = models.BooleanField(default=False)
    descripcion_hechos = models.TextField(null=True, blank=True)
    valoracion_hechos = models.TextField(null=True, blank=True)
    formas_accidente = models.TextField(null=True, blank=True)
    analisis_causas = models.TextField(null=True, blank=True)
    causas_accidente = models.TextField(null=True, blank=True)
    aplicar_accion = models.TextField(null=True, blank=True)
    itinere = models.BooleanField(default=False)
    tipo_suceso = models.TextField(null=True, blank=True)
    creador = models.TextField(null=True, blank=True)
    fecha_investigacion = models.CharField(max_length=16, null=True)
    otros = models.BooleanField(default=False)
    empresa = models.TextField(null=True, blank=True)
    parte_cuerpo = models.TextField(null=True, blank=True)
    agente = models.TextField(null=True, blank=True)
    forma_producirse = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"Expediente de {self.trabajador.nombre}"
    
    
class Imagenes(models.Model):
    id = models.CharField(primary_key=True, max_length=37)
    expediente = models.ForeignKey(Expediente, on_delete=models.CASCADE, related_name='imagen')
    imagen = models.ImageField(upload_to='imagenes/')
    
class PuestoTrabajo(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.TextField()
    
class LugarAccidente(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.TextField()

class FormaProducirseAccidente(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.TextField()
    
class CausasProducenAccidente(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.TextField()

class Creador(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.TextField()

class ParteCuerpo(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.TextField()

class Agente(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.TextField()

class FormaProducirse(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.TextField()

