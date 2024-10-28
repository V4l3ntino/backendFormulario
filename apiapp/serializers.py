from rest_framework import serializers
from .models import Trabajador, Expediente, Imagenes, PuestoTrabajo, LugarAccidente, FormaProducirseAccidente, CausasProducenAccidente

class TrabajadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trabajador
        fields = ('id', 'nombre', 'apellido', 'experiencia')
        
        
class ExpedienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expediente
        fields = (
            'id', 
            'trabajador', 
            'sexo', 
            'edad', 
            'puesto_trabajo',
            'lugar_accidente', 
            'fecha_suceso', 
            'lesion', 
            'lesionado_check', 
            'descripcion_hechos', 
            'valoracion_hechos', 
            'formas_accidente', 
            'analisis_causas',
            'causas_accidente',
            'aplicar_accion',
            'itinere'
            )
        
class ImagenesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagenes
        fields = ('id', 'expediente', 'imagen')
        
        
class PuestoTrabajoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PuestoTrabajo
        fields = ('id', 'nombre')
        
class LugarAccidenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = LugarAccidente
        fields = ('id', 'nombre')
        
class FormaProducirseAccidenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormaProducirseAccidente
        fields = ('id', 'nombre')

class CausasProducenAccidenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CausasProducenAccidente
        fields = ('id', 'nombre')