# Generated by Django 4.2.2 on 2023-06-27 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Roel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('calle', models.CharField(max_length=30)),
                ('país', models.CharField(max_length=30)),
            ],
        ),
        migrations.RenameField(
            model_name='stock',
            old_name='camada',
            new_name='cantidad',
        ),
    ]
