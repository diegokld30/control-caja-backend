from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from apps.categoria.models import Categoria

from apps.producto.models import Producto
from apps.transacciones.api.serializer import ProductoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticated]