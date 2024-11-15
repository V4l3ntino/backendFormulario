from rest_framework import viewsets, permissions, status
from .models import Trabajador, Expediente, Imagenes, PuestoTrabajo, LugarAccidente, FormaProducirseAccidente, CausasProducenAccidente, Creador, ParteCuerpo, Agente, FormaProducirse
from .serializers import TrabajadorSerializer, ExpedienteSerializer, ImagenesSerializer, PuestoTrabajoSerializer, LugarAccidenteSerializer, FormaProducirseAccidenteSerializer, CausasProducenAccidenteSerializer, CreadorSerializer, ParteCuerpoSerializer, AgenteSerializer, FormaProducirseSerializer
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
    
class LugarAccidenteViewSet(viewsets.ModelViewSet):
    queryset = LugarAccidente.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = LugarAccidenteSerializer
    @action(detail=False, methods=['delete'])
    def deleteall(self, request):
        LugarAccidente.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class FormaProducirseAccidenteViewSet(viewsets.ModelViewSet):
    queryset = FormaProducirseAccidente.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = FormaProducirseAccidenteSerializer
    @action(detail=False, methods=['delete'])
    def deleteall(self, request):
        FormaProducirseAccidente.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CausasProducenAccidenteViewSet(viewsets.ModelViewSet):
    queryset = CausasProducenAccidente.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CausasProducenAccidenteSerializer
    @action(detail=False, methods=['delete'])
    def deleteall(self, request):
        CausasProducenAccidente.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CreadorViewSet(viewsets.ModelViewSet):
    queryset = Creador.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CreadorSerializer
    @action(detail=False, methods=['delete'])
    def deleteall(self, request):
        Creador.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ParteCuerpoViewSet(viewsets.ModelViewSet):
    queryset = ParteCuerpo.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ParteCuerpoSerializer
    @action(detail=False, methods=['delete'])
    def deleteall(self, request):
        ParteCuerpo.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AgenteViewSet(viewsets.ModelViewSet):
    queryset = Agente.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AgenteSerializer
    @action(detail=False, methods=['delete'])
    def deleteall(self, request):
        Agente.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class FormaProducirseViewSet(viewsets.ModelViewSet):
    queryset = FormaProducirse.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = FormaProducirseSerializer
    @action(detail=False, methods=['delete'])
    def deleteall(self, request):
        FormaProducirse.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
