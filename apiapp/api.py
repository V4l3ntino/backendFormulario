from rest_framework import viewsets, permissions, status
from .models import Trabajador, Expediente, Imagenes, PuestoTrabajo
from .serializers import TrabajadorSerializer, ExpedienteSerializer, ImagenesSerializer, PuestoTrabajoSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


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
    
class PuestoTrabajoViewSet(viewsets.ModelViewSet):
    queryset = PuestoTrabajo.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PuestoTrabajoSerializer
    @action(detail=False, methods=['delete'])
    def deleteall(self, request):
        PuestoTrabajo.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)