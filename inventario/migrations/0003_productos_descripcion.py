# Generated by Django 4.2 on 2024-09-18 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0002_rename_id_producto_productos_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='descripcion',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
