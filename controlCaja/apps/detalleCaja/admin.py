from django.contrib import admin
from .models import DetalleCaja

@admin.register(DetalleCaja)
class DetalleCajaAdmin(admin.ModelAdmin):
    list_display = ('id', 'caja_id', 'tipo', 'descripcion_corta', 'monto', 'fecha')
    list_filter = ('tipo', 'fecha', 'caja_id')
    search_fields = ('descripcion',)
    ordering = ('-fecha',)

    def descripcion_corta(self, obj):
        return (obj.descripcion[:50] + '...') if len(obj.descripcion) > 50 else obj.descripcion
    descripcion_corta.short_description = 'Descripción'
