from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.categoria.models import Categoria
from apps.categoria.api.serializer import CategoriaSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [IsAuthenticated]