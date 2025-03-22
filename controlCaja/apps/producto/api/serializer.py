from rest_framework import serializers
from apps.categoria.models import Categoria

from apps.categoria.api.serializer import CategoriaSerializer

from apps.producto.models import Producto


class ProductoSerializer(serializers.ModelSerializer):
    categoria_id = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all(), write_only=True)

    class Meta:
        model = Producto
        fields = [
            'id',
            'nombre',
            'categoria_id',
            'precio_compra',
            'precio_venta',
            'stock'
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        representation['categoria'] = CategoriaSerializer(instance.categoria).data if instance.categoria_id else None

        representation.pop('categoria_id', None)

        return representation