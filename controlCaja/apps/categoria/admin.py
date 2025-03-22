from django.contrib import admin
from django.contrib import admin
from .models import Categoria

# Register your models here.
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    list_filter = ('nombre',)
    search_fields = ('nombre',)
