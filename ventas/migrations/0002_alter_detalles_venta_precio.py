# Generated by Django 5.1 on 2024-09-19 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalles_venta',
            name='precio',
            field=models.PositiveIntegerField(),
        ),
    ]
