# apps/detalleCaja/api/serializer.py
from rest_framework import serializers
from apps.detalleCaja.models import DetalleCaja
from apps.cajaDiaria.models import CajaDiaria



class DetalleCajaSerializer(serializers.ModelSerializer):
    caja_id = serializers.PrimaryKeyRelatedField(queryset=CajaDiaria.objects.all(), write_only=True)

    class Meta:
        model = DetalleCaja  # Corregido aquí
        fields = [
            'id', 'caja_id', 'descripcion', 'tipo', 'monto', 'fecha'
        ]

    # Representación detallada en GET
    def to_representation(self, instance):
        representation = super().to_representation(instance)

        # Detalle completo de la CajaDiaria (anidado)
        representation['caja'] = CajaDiariaSerializer(instance.caja_id).data if instance.caja_id else None

        # Remueve "caja_id" para evitar duplicados (opcional)
        representation.pop('caja_id', None)

        return representation
