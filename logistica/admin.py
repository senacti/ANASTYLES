from django.contrib import admin
from .models import Estate_log,Client,Pedidos,Details_pedidos,Logistic

admin.site.register(Estate_log)
admin.site.register(Client)
admin.site.register(Pedidos)
admin.site.register(Details_pedidos)
admin.site.register(Logistic)

# Register your models here.
