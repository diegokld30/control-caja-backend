from django.db import models
from django.db.models import SET_NULL

from apps.users.models import User
from apps.producto.models import Producto

class tipoTransaccion(models.TextChoices):
    VENTA = 'venta', 'Venta'
    COMPRA = 'compra', 'Compra'
    DEVOLUCION = 'devolucion', 'Devolucion'
    AJUSTE = 'ajuste', 'Ajuste'

class Transaccion(models.Model):
    tipo = models.CharField(max_length=20, choices=tipoTransaccion.choices, default=tipoTransaccion.VENTA)
    producto_id = models.ForeignKey(Producto, on_delete=SET_NULL, null=True)
    cantidad = models.IntegerField(default=0)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    fecha = models.DateField(auto_now_add=True)
    usuario_id = models.ForeignKey(User, on_delete=SET_NULL, null=True)

    def __str__(self):
        return self.tipo
