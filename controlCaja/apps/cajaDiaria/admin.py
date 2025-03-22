# apps/cajaDiaria/admin.py
from django.contrib import admin
from .models import CajaDiaria

@admin.register(CajaDiaria)
class CajaDiariaAdmin(admin.ModelAdmin):
    list_display = ['fecha_apertura', 'fecha_cierre', 'saldo_inicial', 'saldo_final', 'abierta_por', 'cerrada_por']
    list_filter = ['fecha_apertura', 'fecha_cierre', 'abierta_por', 'cerrada_por']
    search_fields = ['observaciones']
