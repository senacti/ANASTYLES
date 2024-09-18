from django.contrib import admin
from .models import Talla, Color, Estado, Produccion, Categoria

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Talla)
class TallaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo')
    search_fields = ('nombre',)

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'codigo_hex')
    search_fields = ('nombre',)

@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Produccion)
class ProduccionAdmin(admin.ModelAdmin):
        list_display = ('nombre', 'color', 'talla', 'cantidad', 'fecha_produccion', 'fecha_finalizacion', 'estado')
        search_fields = ('nombre','color', 'talla', 'estado', 'fecha_produccion')
        list_filter = ('nombre', 'categoria', 'estado',)

        def get_queryset(self, request):
            qs = super().get_queryset(request)
            return qs.select_related('color', 'talla', 'estado')