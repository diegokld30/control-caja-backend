from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from django.db.models import Sum, F
from apps.cajaDiaria.models import CajaDiaria
from apps.cajaDiaria.api.serializer import CajaDiariaSerializer
from rest_framework.permissions import IsAuthenticated
from apps.transacciones.models import Transaccion
from apps.detalleCaja.models import DetalleCaja
from apps.detalleCaja.api.serializer import DetalleCajaSerializer


class CajaDiariaViewSet(viewsets.ModelViewSet):
    queryset = CajaDiaria.objects.all().order_by('-fecha_apertura')
    serializer_class = CajaDiariaSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['post'], url_path="cerrar")
    def cerrar(self, request):
        """
        Acción para cerrar la caja abierta.
        Se busca la caja con fecha_cierre nula, se calculan ingresos y egresos a partir de las transacciones
        y se actualiza la caja con saldo_final y fecha_cierre. Además, se crea un registro en DetalleCaja con el consolidado.
        """
        # Buscamos la caja abierta (suponiendo que solo puede haber una caja abierta a la vez)
        caja = CajaDiaria.objects.filter(fecha_cierre__isnull=True).order_by('-fecha_apertura').first()
        if not caja:
            return Response({"detail": "No hay caja abierta para cerrar."}, status=status.HTTP_400_BAD_REQUEST)

        # Obtener transacciones del día de la caja abierta. Por ejemplo, desde la apertura hasta ahora.
        transacciones = Transaccion.objects.filter(fecha__gte=caja.fecha_apertura, fecha__lte=timezone.now())

        # Calcular ingresos y egresos. Este ejemplo asume:
        # - Los ingresos se derivan de las transacciones de tipo "venta"
        # - Los egresos se derivan de las transacciones de tipo "compra"
        ingresos = transacciones.filter(tipo="venta").aggregate(
            total=Sum(F("precio_unitario") * F("cantidad"))
        )["total"] or 0
        egresos = transacciones.filter(tipo="compra").aggregate(
            total=Sum(F("precio_unitario") * F("cantidad"))
        )["total"] or 0

        print(ingresos)

        saldo_final = (caja.saldo_inicial + ingresos) - egresos

        # Actualizar la caja
        caja.fecha_cierre = timezone.now()
        caja.saldo_final = saldo_final
        caja.save()

        # Crear el registro consolidado en DetalleCaja (puedes ajustar la descripción y tipo según tu necesidad)
        detalle = DetalleCaja.objects.create(
            caja_id=caja,
            transaccion_id=None,  # Si no relacionas una transacción específica para el cierre
            descripcion="Cierre de caja",
            tipo="ingreso",  # O podrías usar un tipo especial "cierre"
            monto=saldo_final,
        )
        serializer = DetalleCajaSerializer(detalle)
        return Response(serializer.data, status=status.HTTP_200_OK)
