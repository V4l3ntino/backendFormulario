from rest_framework import routers
from django.urls import path
from .api import TrabajadorViewSet, ExpedienteViewSet, ImagenesViewSet, PuestoTrabajoViewSet
from .views import ObtenerTrabajadorPorId

router = routers.DefaultRouter()

router.register('api/trabajador', TrabajadorViewSet, 'apiTrabajador')
router.register('api/expediente', ExpedienteViewSet, 'apiExpediente')
router.register('api/imagenes', ImagenesViewSet, 'apiImagenes')
router.register('api/puesto_trabajo', PuestoTrabajoViewSet, 'apiPuestoTrabajo')

urlpatterns = router.urls
urlpatterns += [
    path('api/expediente/generate-word-document/<str:id>/', ObtenerTrabajadorPorId.as_view(), name='obtenerTrabajadorPorId'),
]