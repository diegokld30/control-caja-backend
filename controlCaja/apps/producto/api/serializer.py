from rest_framework import serializers
from apps.categoria.models import Categoria
from apps.categoria.api.serializer import CategoriaSerializer
from apps.producto.models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    # Campo para escritura: se envía el id de la categoría
    categoria_id = serializers.PrimaryKeyRelatedField(
        queryset=Categoria.objects.all(), write_only=False
    )
    # Campo para lectura: se muestra la representación completa de la categoría
    categoria = CategoriaSerializer(source="categoria_id", read_only=True)

    class Meta:
        model = Producto
        fields = [
            'id',
            'nombre',
            'categoria_id',
            'categoria',
            'precio_compra',
            'precio_venta',
            'stock'
        ]
