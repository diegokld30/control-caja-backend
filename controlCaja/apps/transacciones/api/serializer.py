# src/apps/transacciones/api/serializer.py
from rest_framework import serializers
from apps.transacciones.models import Transaccion
from apps.producto.models import Producto
from apps.users.models import User
from apps.producto.api.serializer import ProductoSerializer
from apps.users.api.serializer import UserSerializer

class TransaccionSerializer(serializers.ModelSerializer):
    # Para escritura, se recibe el id de las relaciones
    producto_id = serializers.PrimaryKeyRelatedField(
        queryset=Producto.objects.all(), write_only=True
    )
    usuario_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), write_only=True
    )

    # Para lectura, se muestran las representaciones completas
    producto = ProductoSerializer(source="producto_id", read_only=True)
    usuario = UserSerializer(source="usuario_id", read_only=True)

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
            'producto',
            'usuario'
        ]

    def create(self, validated_data):
        """
        Al crear una transacción, si el tipo es 'venta' se descuenta la cantidad
        del stock del producto. Si el stock es insuficiente, se lanza un error.
        """
        producto = validated_data.get('producto_id')
        cantidad = validated_data.get('cantidad', 0)
        tipo = validated_data.get('tipo')

        if tipo == "venta" and producto and cantidad:
            # Verificamos stock suficiente
            if producto.stock < cantidad:
                raise serializers.ValidationError("No hay suficiente stock para realizar la venta.")
            # Descontamos la cantidad vendida
            producto.stock -= cantidad
            producto.save()

        # Opcional: si quisieras manejar otros tipos (por ejemplo, "compra" que aumente el stock),
        # podrías agregar condiciones adicionales aquí.

        return super().create(validated_data)
