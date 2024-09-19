from django.urls import path
from .views import ProductosListView

urlpatterns = [
    path('productos/', ProductosListView.as_view(), name='productos_list'),
]