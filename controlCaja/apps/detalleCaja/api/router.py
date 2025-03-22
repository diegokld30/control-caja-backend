# apps/detalleCaja/api/router.py
from rest_framework.routers import DefaultRouter
from .views import DetalleCajaViewSet

router = DefaultRouter()
router.register(r'detallecaja', DetalleCajaViewSet, basename='detallecaja')

urlpatterns = router.urls
