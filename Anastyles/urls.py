from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import indexx

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', indexx, name='index'),
    path('inventario/', include('inventario.urls')),
    path('logistica/', include('logistica.urls')),
    path('produccion/', include('produccion.urls')),
    path('usuario/', include('usuarios.urls')),
    path('ventas/', include('ventas.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
