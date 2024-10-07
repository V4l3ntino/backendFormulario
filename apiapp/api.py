from rest_framework import viewsets, permissions
from .models import Trabajador, Expediente, Imagenes
from .serializers import TrabajadorSerializer, ExpedienteSerializer, ImagenesSerializer

class TrabajadorViewSet(viewsets.ModelViewSet):
    queryset = Trabajador.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TrabajadorSerializer
    
    
class ExpedienteViewSet(viewsets.ModelViewSet):
    queryset = Expediente.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ExpedienteSerializer
    
class ImagenesViewSet(viewsets.ModelViewSet):
    queryset = Imagenes.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ImagenesSerializer