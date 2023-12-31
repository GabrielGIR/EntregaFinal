# Generated by Django 4.2.2 on 2023-07-14 22:28

import Roel.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Roel', '0004_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, null=True)),
                ('precio', models.FloatField(max_length=8, null=True)),
                ('categoria', models.CharField(choices=[('Pulsera', 'Pulsera'), ('Collar', 'Collar'), ('Pendiente', 'Pendiente'), ('Pañuelo', 'Pañulo')], max_length=200, null=True)),
                ('descripcion', models.CharField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.CreateModel(
            name='Ordenar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name=Roel.models.Producto)),
                ('estado', models.CharField(choices=[('Pendiente', 'Pendiente'), ('No se puede entregar', 'No se puede entregar'), ('Entreado', 'Entregado')], max_length=200, null=True)),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Roel.cliente')),
                ('producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Roel.producto')),
            ],
        ),
    ]
