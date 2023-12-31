# Generated by Django 4.2.2 on 2023-07-31 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Roel', '0013_alter_producto_categoria'),
    ]

    operations = [
        migrations.CreateModel(
            name='SolicitudDistribuidora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('profesion', models.CharField(max_length=30)),
                ('aprobado', models.BooleanField(default=False)),
            ],
        ),
    ]
