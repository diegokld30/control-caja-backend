from django.db import models
from apps.users.models import User

class CajaDiaria(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_apertura = models.DateTimeField(auto_now_add=True)
    fecha_cierre = models.DateTimeField(null=True, blank=True)
    saldo_inicial = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    saldo_final = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    abierta_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='cajas_abiertas')
    cerrada_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='cajas_cerradas')
    observaciones = models.TextField(blank=True)

    def __str__(self):
        return self.nombre
       # return f"Caja abierta el {self.fecha_apertura.strftime('%Y-%m-%d %H:%M:%S')}"

