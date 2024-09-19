from django.contrib import admin
from .models import Venta, detalles_venta

admin.site.register(Venta)
admin.site.register(detalles_venta)
