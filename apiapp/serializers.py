from rest_framework import serializers
from .models import Trabajador, Expediente 

class TrabajadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trabajador
        fields = ('id', 'nombre', 'apellido', 'experiencia')
        
        
class ExpedienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expediente
        fields = ('id', 'trabajador', 'sexo', 'edad', 'lugar_accidente', 'fecha_suceso', 'lesion', 'descripcion_hechos')