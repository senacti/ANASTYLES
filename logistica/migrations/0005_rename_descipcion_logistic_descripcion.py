# Generated by Django 4.2 on 2024-09-19 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logistica', '0004_details_pedidos_id_pedido'),
    ]

    operations = [
        migrations.RenameField(
            model_name='logistic',
            old_name='Descipcion',
            new_name='Descripcion',
        ),
    ]
