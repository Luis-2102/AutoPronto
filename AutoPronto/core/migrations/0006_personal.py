# Generated by Django 5.0.2 on 2024-03-15 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_preguntas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100, verbose_name='Nombre')),
                ('dep', models.CharField(max_length=100, verbose_name='Departamento')),
                ('des', models.CharField(max_length=100, verbose_name='Descripción')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificacion')),
            ],
            options={
                'verbose_name': 'Personal',
                'verbose_name_plural': 'Personal',
                'ordering': ['-created'],
            },
        ),
    ]
