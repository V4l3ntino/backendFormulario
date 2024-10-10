from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Trabajador, Expediente
from .serializers import TrabajadorSerializer, ExpedienteSerializer
import subprocess
import json
# Create your views here.
class ObtenerTrabajadorPorId(APIView):
    def post(self, request, id):
        try:
            expediente = Expediente.objects.get(id=id)
            
            tipo_lesion = [0,0,0,0]
            
            lesion = expediente.lesion.split("|")
            
            if(lesion[0].strip() == "Leve"):
                tipo_lesion[0] = 1
            
            hora = ""
            fecha = ""
            
            if(expediente.fecha_suceso):
                hora = expediente.fecha_suceso.split("T")[1]
                fecha = expediente.fecha_suceso.split("T")[0]
            
            data = {
                "nombre_trabajador": f"{expediente.trabajador.apellido}, {expediente.trabajador.nombre}",
                "puesto_trabajo": expediente.lugar_accidente,
                "edad": expediente.edad,
                "experiencia": expediente.trabajador.experiencia,
                "lugar_accidente": expediente.lugar_accidente,
                "hora_accidente": f"{hora}",
                "fecha_accidente": f"{fecha}",
                "lesion": lesion[1],
                "sexo": expediente.sexo,
                "tipo_lesion": tipo_lesion
            }
            
            path_file = "json/expediente.json"
            
            with open(path_file, 'w') as f:
                json.dump(data, f, indent=4)
                
            
            subprocess.run(['python', 'C:\\Users\\varmido\\Desktop\\APP_Formulario\\backend\\prueba.py'], check=True)            
            return Response(status=status.HTTP_200_OK)
        except Trabajador.DoesNotExist:
            return Response({'error': 'Expediente no encontrado'}, status=status.HTTP_404_NOT_FOUND)