# Generated by Django 4.2.2 on 2023-07-31 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Roel', '0012_remove_distribuidora_apellido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='categoria',
            field=models.CharField(choices=[('Pulsera', 'Pulsera'), ('Collar', 'Collar'), ('Pendiente', 'Pendiente'), ('Electrodomestico', 'Electrodomestico'), ('Mueble', 'Mueble'), ('Focos', 'Focos'), ('Comestibles', 'Comestibles')], max_length=200, null=True),
        ),
    ]
