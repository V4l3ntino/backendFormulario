from rest_framework import serializers
from .models import Trabajador, Expediente, Imagenes, PuestoTrabajo

class TrabajadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trabajador
        fields = ('id', 'nombre', 'apellido', 'experiencia')
        
        
class ExpedienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expediente
        fields = ('id', 'trabajador', 'sexo', 'edad', 'puesto_trabajo','lugar_accidente', 'fecha_suceso', 'lesion', 'lesionado_check', 'descripcion_hechos')
        
class ImagenesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagenes
        fields = ('id', 'expediente', 'imagen')
        
        
class PuestoTrabajoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PuestoTrabajo
        fields = ('id', 'nombre')