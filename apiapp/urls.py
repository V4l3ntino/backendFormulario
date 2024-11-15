from rest_framework import routers
from django.urls import path
from .api import TrabajadorViewSet, ExpedienteViewSet, ImagenesViewSet, PuestoTrabajoViewSet, LugarAccidenteViewSet, FormaProducirseAccidenteViewSet, CausasProducenAccidenteViewSet, CreadorViewSet, ParteCuerpoViewSet, AgenteViewSet, FormaProducirseViewSet
from .views import ObtenerTrabajadorPorId

router = routers.DefaultRouter()

router.register('api/trabajador', TrabajadorViewSet, 'apiTrabajador')
router.register('api/expediente', ExpedienteViewSet, 'apiExpediente')
router.register('api/imagenes', ImagenesViewSet, 'apiImagenes')
router.register('api/puesto_trabajo', PuestoTrabajoViewSet, 'apiPuestoTrabajo')
router.register('api/lugar_accidente', LugarAccidenteViewSet, 'apiLugarAccidente')
router.register('api/forma_producirse_accidente', FormaProducirseAccidenteViewSet, 'apiFormaProducirseAccidente')
router.register('api/causas_accidente', CausasProducenAccidenteViewSet, 'apiCausasAccidente')
router.register('api/creador', CreadorViewSet, 'apiCreador')
router.register('api/parte_cuerpo', ParteCuerpoViewSet, 'parteCuerpo')
router.register('api/agente', AgenteViewSet, 'agente')
router.register('api/forma_producirse', FormaProducirseViewSet, 'formaProducirse')

urlpatterns = router.urls
urlpatterns += [
    path('api/expediente/generate-word-document/<str:id>/<str:tipo>', ObtenerTrabajadorPorId.as_view(), name='obtenerTrabajadorPorId'),
]