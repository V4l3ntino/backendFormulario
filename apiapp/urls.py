from rest_framework import routers
from .api import TrabajadorViewSet
router = routers.DefaultRouter()

router.register('api/trabajador', TrabajadorViewSet, 'apiTrabajador')

urlpatterns = router.urls