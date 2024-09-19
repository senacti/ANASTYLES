from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Talla, Color, Estado, Produccion, Categoria

class CategoriaResource(resources.ModelResource):
    class Meta:
        model = Categoria

class TallaResource(resources.ModelResource):
    class Meta:
        model = Talla

class ColorResource(resources.ModelResource):
    class Meta:
        model = Color

class EstadoResource(resources.ModelResource):
    class Meta:
        model = Estado

class ProduccionResource(resources.ModelResource):
    class Meta:
        model = Produccion

@admin.register(Categoria)
class CategoriaAdmin(ImportExportModelAdmin):
    resource_class = CategoriaResource
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Talla)
class TallaAdmin(ImportExportModelAdmin):
    resource_class = TallaResource
    list_display = ('nombre', 'tipo')
    search_fields = ('nombre',)

@admin.register(Color)
class ColorAdmin(ImportExportModelAdmin):
    resource_class = ColorResource
    list_display = ('nombre', 'codigo_hex')
    search_fields = ('nombre',)

@admin.register(Estado)
class EstadoAdmin(ImportExportModelAdmin):
    resource_class = EstadoResource
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Produccion)
class ProduccionAdmin(ImportExportModelAdmin):
        list_display = ('nombre', 'color', 'talla', 'cantidad', 'fecha_produccion', 'fecha_finalizacion', 'estado')
        search_fields = ('nombre','color', 'talla', 'estado', 'fecha_produccion')
        list_filter = ('nombre', 'categoria', 'estado',)

        def get_queryset(self, request):
            qs = super().get_queryset(request)
            return qs.select_related('color', 'talla', 'estado')