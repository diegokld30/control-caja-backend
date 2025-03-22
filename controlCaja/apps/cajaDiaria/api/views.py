# apps/cajaDiaria/api/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from apps.cajaDiaria.models import CajaDiaria
from apps.cajaDiaria.api.serializer import CajaDiariaSerializer

class CajaDiariaViewSet(viewsets.ModelViewSet):
    queryset = CajaDiaria.objects.all().order_by('-fecha_apertura')
    serializer_class = CajaDiariaSerializer
    permission_classes = [IsAuthenticated]
