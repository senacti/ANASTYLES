from django.db import models
from produccion.models import Produccion

class Productos(models.Model):
    id = models.AutoField(primary_key=True)
    id_product = models.ForeignKey(Produccion, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.descripcion
    
class Ubicacion_inv(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class Inventario(models.Model):
    id = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    id_ubicacion = models.ForeignKey(Ubicacion_inv, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion




 
