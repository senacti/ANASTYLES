from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Venta, detalles_venta

class VentaResource(resources.ModelResource):
    class Meta:
        model = Venta

class DetallesVentaResource(resources.ModelResource):
    class Meta:
        model = detalles_venta

@admin.register(Venta)
class VentasAdmin(ImportExportModelAdmin):
    resource_class = VentaResource
    list_display = ('id', 'descripcion', 'id_cliente', 'fecha_venta', 'total_venta')
    search_fields = ('descripcion', 'id_cliente__nombre')
    list_filter = ('fecha_venta', 'id_cliente')

@admin.register(detalles_venta)
class DetallesVentaAdmin(ImportExportModelAdmin):
    resource_class = DetallesVentaResource
    list_display = ('id', 'id_venta', 'id_product', 'cantidad', 'precio', 'descripcion')
    search_fields = ('id_venta__descripcion', 'id_product__descripcion')
    list_filter = ('id_venta', 'id_product')