# apps/detalleCaja/api/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from apps.detalleCaja.models import DetalleCaja
from apps.detalleCaja.api.serializer import DetalleCajaSerializer

class DetalleCajaViewSet(viewsets.ModelViewSet):
    queryset = DetalleCaja.objects.all()
    serializer_class = DetalleCajaSerializer
    permission_classes = [IsAuthenticated]
