from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from apps.transacciones.models import Transaccion
from apps.transacciones.api.serializer import TransaccionSerializer

class TransaccionViewSet(viewsets.ModelViewSet):
    queryset = Transaccion.objects.all()
    serializer_class = TransaccionSerializer
    permission_classes = [IsAuthenticated]