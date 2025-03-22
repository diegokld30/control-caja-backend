from django.contrib import admin
from .models import Transaccion

# Register your models here.
@admin.register(Transaccion)
class TransaccionAdmin(admin.ModelAdmin):
    list_display = ('producto_id', 'cantidad', 'precio_unitario', 'usuario_id',)
    list_filter = ('producto_id', 'precio_unitario', 'usuario_id',)
    search_fields = ('producto_id', 'precio_unitario', 'usuario_id',)
