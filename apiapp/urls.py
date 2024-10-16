from rest_framework import routers
from django.urls import path
from .api import TrabajadorViewSet, ExpedienteViewSet, ImagenesViewSet, PuestoTrabajoViewSet, LugarAccidenteViewSet, FormaProducirseAccidenteViewSet
from .views import ObtenerTrabajadorPorId

router = routers.DefaultRouter()

router.register('api/trabajador', TrabajadorViewSet, 'apiTrabajador')
router.register('api/expediente', ExpedienteViewSet, 'apiExpediente')
router.register('api/imagenes', ImagenesViewSet, 'apiImagenes')
router.register('api/puesto_trabajo', PuestoTrabajoViewSet, 'apiPuestoTrabajo')
router.register('api/lugar_accidente', LugarAccidenteViewSet, 'apiLugarAccidente')
router.register('api/forma_producirse_accidente', FormaProducirseAccidenteViewSet, 'apiFormaProducirseAccidente')

urlpatterns = router.urls
urlpatterns += [
    path('api/expediente/generate-word-document/<str:id>/', ObtenerTrabajadorPorId.as_view(), name='obtenerTrabajadorPorId'),
]