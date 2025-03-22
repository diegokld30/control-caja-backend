from django.contrib import admin
from .models import Producto
# Register your models here.
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre','categoria_id','precio_compra','precio_venta','stock')
    list_filter = ('nombre','categoria_id',)
    search_fields = ('nombre','categoria_id',)

