from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('invetario/', include('inventario.urls')),
    path('logistica/', include('logistica.urls')),
    path('produccion/', include('produccion.urls')),
    path('usuario/', include('usuarios.urls')),
    path('ventas/', include('ventas.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
