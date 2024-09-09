from rest_framework import viewsets, permissions
from .models import Trabajador
from .serializers import TrabajadorSerializer

class TrabajadorViewSet(viewsets.ModelViewSet):
    queryset = Trabajador.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TrabajadorSerializer