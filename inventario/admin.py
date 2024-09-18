from django.contrib import admin
from .models import Productos, Ubicacion_inv,Inventario

admin.site.register(Productos)
admin.site.register(Inventario)
admin.site.register(Ubicacion_inv)

# Register your models here.
