from django.db import models
from inventario.models import Productos
from logistica.models import Client, Pedidos

class Venta(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    id_cliente = models.ForeignKey(Client, on_delete=models.CASCADE)
    fecha_venta = models.DateTimeField()
    total_venta = models.PositiveIntegerField()

    def __str__(self):
        return self.descripcion
    
class detalles_venta(models.Model):
    id = models.AutoField(primary_key=True)
    id_venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    id_product = models.ForeignKey(Productos, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(verbose_name="Cantidad")
    precio = models.PositiveIntegerField()
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion 