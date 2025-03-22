from rest_framework import serializers
from apps.transacciones.models import Transaccion
from apps.users.models import User
from apps.producto.models import Producto

from apps.users.api.serializer import UserSerializer
from apps.producto.api.serializer import ProductoSerializer

class TransaccionSerializer(serializers.ModelSerializer):
    producto_id = serializers.PrimaryKeyRelatedField(queryset=Producto.objects.all(), write_only=True)
    usuario_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True)

    class Meta:
        model = Transaccion
        fields = [
            'id',
            'tipo',
            'producto_id',
            'cantidad',
            'precio_unitario',
            'fecha',
            'usuario_id',
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)


        representation['producto'] = ProductoSerializer(instance.producto_id).data if instance.producto_id else None
        representation['usuario'] = UserSerializer(instance.usuario_id).data if instance.usuario_id else None

        # Removemos los campos originales "_id" para claridad (opcional pero recomendado)
        representation.pop('producto_id', None)
        representation.pop('usuario_id', None)

        return representation
