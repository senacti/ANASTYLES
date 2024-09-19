from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Estate_log, Client, Pedidos, Details_pedidos, Logistic

class EstateLogResource(resources.ModelResource):
    class Meta:
        model = Estate_log

class ClientResource(resources.ModelResource):
    class Meta:
        model = Client

class PedidosResource(resources.ModelResource):
    class Meta:
        model = Pedidos

class DetailsPedidosResource(resources.ModelResource):
    class Meta:
        model = Details_pedidos

class LogisticResource(resources.ModelResource):
    class Meta:
        model = Logistic

@admin.register(Estate_log)
class EstateLogAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = EstateLogResource
    list_display = ('id', 'Nombre')
    search_fields = ('Nombre',)

@admin.register(Client)
class ClientAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = ClientResource
    list_display = ('id', 'cedula', 'nombre', 'apellido', 'telefono', 'correo_electrico')
    search_fields = ('nombre', 'apellido', 'cedula')
    list_filter = ('apellido',)

@admin.register(Pedidos)
class PedidosAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = PedidosResource
    list_display = ('id', 'id_cliente', 'descripcion', 'fecha_pedido')
    search_fields = ('descripcion', 'id_cliente__nombre', 'id_cliente__apellido')
    list_filter = ('fecha_pedido', 'id_cliente')

@admin.register(Details_pedidos)
class DetailsPedidosAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = DetailsPedidosResource
    list_display = ('id', 'id_producto', 'id_pedido', 'descripcion', 'cantidad', 'precio')
    search_fields = ('id_producto__descripcion', 'id_pedido__descripcion')
    list_filter = ('id_producto', 'id_pedido')

@admin.register(Logistic)
class LogisticAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = LogisticResource
    list_display = ('id', 'id_pedido', 'Descripcion', 'id_estado', 'fecha_envio', 'fecha_entrega')
    search_fields = ('Descripcion', 'id_pedido__descripcion', 'id_estado__Nombre')
    list_filter = ('id_pedido', 'id_estado', 'fecha_envio')