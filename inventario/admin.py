from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Productos, Ubicacion_inv, Inventario

class ProductosResource(resources.ModelResource):
    class Meta:
        model = Productos

class UbicacionInvResource(resources.ModelResource):
    class Meta:
        model = Ubicacion_inv

class InventarioResource(resources.ModelResource):
    class Meta:
        model = Inventario

@admin.register(Productos)
class ProductosAdmin(ImportExportModelAdmin):
    resource_class = ProductosResource
    list_display = ('id', 'id_product', 'descripcion', 'precio', 'cantidad')
    search_fields = ('descripcion', 'id_product__nombre')
    list_filter = ('id_product', 'precio')

@admin.register(Ubicacion_inv)
class UbicacionInvAdmin(ImportExportModelAdmin):
    resource_class = UbicacionInvResource
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)

@admin.register(Inventario)
class InventarioAdmin(ImportExportModelAdmin):
    resource_class = InventarioResource
    list_display = ('id', 'id_producto', 'id_ubicacion', 'descripcion')
    search_fields = ('id_producto__descripcion', 'id_ubicacion__nombre')
    list_filter = ('id_producto', 'id_ubicacion')