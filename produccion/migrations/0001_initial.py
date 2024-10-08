# Generated by Django 4.2 on 2024-09-18 08:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('codigo_hex', models.CharField(max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Talla',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('tipo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Produccion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('cantidad', models.PositiveIntegerField(verbose_name='Cantidad')),
                ('fecha_produccion', models.DateField()),
                ('fecha_finalizacion', models.DateField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produccion.categoria')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produccion.color')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produccion.estado')),
                ('talla', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produccion.talla')),
            ],
        ),
    ]
