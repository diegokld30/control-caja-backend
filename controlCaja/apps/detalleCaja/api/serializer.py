# apps/detalleCaja/api/serializer.py

from rest_framework import serializers
from apps.detalleCaja.models import DetalleCaja
from apps.transacciones.api.serializer import TransaccionSerializer

class DetalleCajaSerializer(serializers.ModelSerializer):
    # Para escritura: se envían solo los IDs
    caja_id = serializers.PrimaryKeyRelatedField(
        queryset=DetalleCaja._meta.get_field("caja_id").remote_field.model.objects.all(),
        write_only=True
    )
    transaccion_id = serializers.PrimaryKeyRelatedField(
        queryset=DetalleCaja._meta.get_field("transaccion_id").remote_field.model.objects.all(),
        write_only=True
    )
    # Para lectura: definimos campos calculados
    caja = serializers.SerializerMethodField()
    transaccion = serializers.SerializerMethodField()

    class Meta:
        model = DetalleCaja
        fields = [
            'id',
            'caja_id',
            'transaccion_id',
            'descripcion',
            'tipo',
            'monto',
            'fecha',
            'caja',
            'transaccion',
        ]

    def get_caja(self, obj):
        # Importamos localmente para evitar problemas de importación circular
        from apps.cajaDiaria.api.serializer import CajaDiariaSerializer
        return CajaDiariaSerializer(obj.caja_id).data if obj.caja_id else None

    def get_transaccion(self, obj):
        return TransaccionSerializer(obj.transaccion_id).data if obj.transaccion_id else None
