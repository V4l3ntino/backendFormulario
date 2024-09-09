from rest_framework import serializers
from .models import Trabajador 

class TrabajadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trabajador
        fields = ('id', 'nombre', 'apellido', 'sexo', 'experiencia')