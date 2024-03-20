# Generated by Django 5.0.2 on 2024-03-14 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entregas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tit', models.CharField(max_length=100, verbose_name='Titulo entrega')),
                ('description', models.TextField(verbose_name='descripción entrega')),
                ('img', models.ImageField(upload_to='entregas', verbose_name='Imagen Entregas')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificacion')),
            ],
            options={
                'verbose_name': 'Entrega',
                'verbose_name_plural': 'Entregas',
                'ordering': ['-created'],
            },
        ),
        migrations.AlterModelOptions(
            name='servicio',
            options={'ordering': ['-created'], 'verbose_name': 'Icono Servicio', 'verbose_name_plural': 'Iconos Servicios'},
        ),
        migrations.RemoveField(
            model_name='servicio',
            name='det',
        ),
        migrations.RemoveField(
            model_name='servicio',
            name='img',
        ),
        migrations.AddField(
            model_name='servicio',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='servicio',
            name='icon',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='servicio',
            name='tit',
            field=models.CharField(max_length=100),
        ),
    ]