from rest_framework.routers import DefaultRouter
from .views import TransaccionViewSet

router = DefaultRouter()
router.register(r'transacciones', TransaccionViewSet, basename='transacciones')

urlpatterns = router.urls