from django.db import models
from inventario.models import Productos
from django.core.exceptions import ValidationError

class Estate_log(models.Model):
    id = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.Nombre
    
class Client(models.Model):
    id = models.AutoField(primary_key=True)
    cedula = models.BigIntegerField()
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.BigIntegerField()
    direccion = models.CharField(max_length=100)
    correo_electrico = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    
class Pedidos(models.Model):
    id = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Client,on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=100)
    fecha_pedido = models.DateTimeField()

    def __str__(self):
        return self.descripcion

class Details_pedidos(models.Model):
    id = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey(Productos,on_delete=models.CASCADE)
    id_pedido = models.ForeignKey(Pedidos,on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=100)
    cantidad = models.PositiveIntegerField(verbose_name="Cantidad")
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.descripcion
    
    def save(self, *args, **kwargs):
        # Obtener el producto relacionado
        producto = self.id_producto
        produccion = producto.id_product  # Esto accede al objeto Produccion relacionado
        
        # Verificar si hay suficiente cantidad en el inventario
        if produccion.cantidad >= self.cantidad:
            # Descontar la cantidad pedida del inventario
            produccion.cantidad -= self.cantidad
            produccion.save()  # Guardar los cambios en la tabla Produccion
            self.precio = self.cantidad * producto.precio
        else:
            raise ValidationError('No hay suficiente inventario disponible para este producto.')
        
        # Guardar el pedido después de actualizar el inventario
        super(Details_pedidos, self).save(*args, **kwargs)


class Logistic(models.Model):
    id = models.AutoField(primary_key=True)
    id_pedido = models.ForeignKey(Pedidos,on_delete=models.CASCADE)
    Descipcion = models.CharField(max_length=100)
    id_estado = models.ForeignKey(Estate_log,on_delete=models.CASCADE)
    fecha_envio = models.DateTimeField()
    fecha_entrega = models.DateTimeField(blank=True)

    def __str__(self):
        return self.Descipcion

