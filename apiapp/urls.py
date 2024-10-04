from rest_framework import routers
from .api import TrabajadorViewSet, ExpedienteViewSet
router = routers.DefaultRouter()

router.register('api/trabajador', TrabajadorViewSet, 'apiTrabajador')
router.register('api/expediente', ExpedienteViewSet, 'apiExpediente')

urlpatterns = router.urls