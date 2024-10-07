from rest_framework import routers
from .api import TrabajadorViewSet, ExpedienteViewSet, ImagenesViewSet
router = routers.DefaultRouter()

router.register('api/trabajador', TrabajadorViewSet, 'apiTrabajador')
router.register('api/expediente', ExpedienteViewSet, 'apiExpediente')
router.register('api/imagenes', ImagenesViewSet, 'apiImagenes')

urlpatterns = router.urls