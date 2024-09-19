from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Productos, Inventario, Ubicacion_inv

class ProductosListViews(ListView):
    model = Productos
    template_name = 'inventario/productos_lista.html'


# Create your views here.
