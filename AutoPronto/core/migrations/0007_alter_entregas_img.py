# Generated by Django 5.0.2 on 2024-03-15 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_personal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entregas',
            name='img',
            field=models.ImageField(upload_to='static/img/', verbose_name='Imagen Entregas'),
        ),
    ]
