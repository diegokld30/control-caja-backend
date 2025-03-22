from django.db import models
from django.db.models import SET_NULL

from apps.categoria.models import Categoria
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    categoria_id = models.ForeignKey(Categoria, on_delete=SET_NULL, null=True)
    precio_compra = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nombre