# Generated by Django 5.0.2 on 2024-03-14 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_entregas_alter_servicio_options_remove_servicio_det_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entregas',
            name='img',
            field=models.ImageField(upload_to='entregas/', verbose_name='Imagen Entregas'),
        ),
    ]
