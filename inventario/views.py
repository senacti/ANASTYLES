from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Productos, Inventario, Ubicacion_inv

class ProductosListView(ListView):
    model = Productos
    template_name = 'inventario/productos_list.html'
    context_object_name = 'productos'

class ProductosDetailView(DetailView):
    models = Productos
    template_name = 'inventario/productos_detail.html'

class ProductosCreateView(CreateView):
    model = Productos
    fields = ['id_product', 'descripcion', 'precio', 'cantidad']
    template_name = 'inventario/productos_form.html'
    success_url = reverse_lazy('productos_list')

class ProductosCreateView(CreateView):
    model = Productos
    fields = ['id_product', 'descripcion', 'precio', 'cantidad']
    template_name = 'inventario/productos_form.html'
    success_url = reverse_lazy('productos_list')

class ProductosUpdateView(UpdateView):
    model = Productos
    fields = ['id_product', 'descripcion', 'precio', 'cantidad']
    template_name = 'inventario/productos_form.html'
    success_url = reverse_lazy('productos_list')

class ProductosDeleteView(DeleteView):
    model = Productos
    template_name = 'inventario/productos_confirm_delete.html'
    success_url = reverse_lazy('productos_list')

# Inventario CRUD
class InventarioListView(ListView):
    model = Inventario
    template_name = 'inventario/inventario_list.html'

class InventarioDetailView(DetailView):
    model = Inventario
    template_name = 'inventario/inventario_detail.html'

class InventarioCreateView(CreateView):
    model = Inventario
    fields = ['id_producto', 'id_ubicacion', 'descripcion']
    template_name = 'inventario/inventario_form.html'
    success_url = reverse_lazy('inventario_list')

class InventarioUpdateView(UpdateView):
    model = Inventario
    fields = ['id_producto', 'id_ubicacion', 'descripcion']
    template_name = 'inventario/inventario_form.html'
    success_url = reverse_lazy('inventario_list')

class InventarioDeleteView(DeleteView):
    model = Inventario
    template_name = 'inventario/inventario_confirm_delete.html'
    success_url = reverse_lazy('inventario_list')

# Create your views here.
