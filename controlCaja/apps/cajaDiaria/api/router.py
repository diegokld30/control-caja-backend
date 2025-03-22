# apps/cajaDiaria/api/router.py
from rest_framework.routers import DefaultRouter
from .views import CajaDiariaViewSet

router = DefaultRouter()
router.register(r'cajadiaria', CajaDiariaViewSet, basename='cajadiaria')

urlpatterns = router.urls
