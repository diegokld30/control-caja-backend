from rest_framework import serializers
from apps.cajaDiaria.models import CajaDiaria
from apps.users.models import User
from apps.users.api.serializer import UserSerializer

class CajaDiariaSerializer(serializers.ModelSerializer):
    # Mantener campos de escritura simples (solo IDs)
    abierta_por = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True)
    cerrada_por = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True, allow_null=True, required=False)

    class Meta:
        model = CajaDiaria
        fields = [
            'id',
            'fecha_apertura',
            'fecha_cierre',
            'saldo_inicial',
            'saldo_final',
            'abierta_por',
            'cerrada_por',
            'observaciones'
        ]

    # Método clave para convertir IDs en objetos completos en las respuestas (lectura)
    def to_representation(self, instance):
        representation = super().to_representation(instance)

        # Ahora reemplazas el ID por el objeto completo serializado
        representation['abierta_por'] = UserSerializer(instance.abierta_por).data if instance.abierta_por else None
        representation['cerrada_por'] = UserSerializer(instance.cerrada_por).data if instance.cerrada_por else None

        return representation
