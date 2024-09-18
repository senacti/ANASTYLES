from django.core.exceptions import ValidationError
from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

TIP_TALLAS = [
    ('numerico', 'numerico'),
    ('letreado', 'letreado')
]

class Talla(models.Model):
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50, choices=TIP_TALLAS)

    def __str__(self):
        return self.nombre

class Color(models.Model):
    nombre = models.CharField(max_length=50)
    codigo_hex = models.CharField(max_length=7)

    def __str__(self):
        return self.nombre

class Estado(models.Model):
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

GENERO = [
    ('hombre', 'hombre'),
    ('mujer', 'mujer'),
    ('niño', 'niño'),
    ('niña', 'niña')
    ]

class Produccion(models.Model):
    id = models.AutoField(primary_key=True)
    id_producto = models.IntegerField()
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    talla = models.ForeignKey(Talla, on_delete=models.CASCADE)
    genero = models.CharField(max_length=30, choices=GENERO)
    cantidad =  models.PositiveIntegerField(verbose_name="Cantidad")
    fecha_produccion = models.DateField()
    fecha_finalizacion = models.DateField()
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    def clean(self):
        super().clean()
        if self.fecha_finalizacion < self.fecha_produccion:
            raise ValidationError('La fecha de finalización no puede ser anterior a la fecha de producción.')
        
    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre