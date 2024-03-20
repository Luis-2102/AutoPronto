from django.contrib import admin
from .models import Servicio , Entregas, Testimonios, Preguntas, Ventajas, Galeria
# Register your models here.

@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('tit', 'description', 'icon',  'created', 'updated')
    search_fields = ('tit', 'description', 'icon')
    list_filter = ('created', 'updated')

@admin.register(Entregas)
class EntregaAdmin(admin.ModelAdmin):
    list_display = ('tit', 'description', 'img',  'created', 'updated')
    search_fields = ('tit', 'description', 'img')
    list_filter = ('created', 'updated')

@admin.register(Testimonios)
class EntregaAdmin(admin.ModelAdmin):
    list_display = ('nom', 'ocu', 'tes', 'img', 'created', 'updated')
    search_fields = ('nom', 'ocu', 'tes','img')
    list_filter = ('created', 'updated')

@admin.register(Preguntas)
class EntregaAdmin(admin.ModelAdmin):
    list_display = ('pre', 'res',  'created', 'updated')
    search_fields = ('pre', 'res')
    list_filter = ('created', 'updated')
    

@admin.register(Ventajas)
class VentajasAdmin(admin.ModelAdmin):
    list_display = ('tit', 'description', 'icon',  'created', 'updated')
    search_fields = ('tit', 'description', 'icon')
    list_filter = ('created', 'updated')

@admin.register(Galeria)
class GaleriaAdmin(admin.ModelAdmin):
    list_display = ('nom','img', 'created', 'updated')
    search_fields = ('nom','img')
    list_filter = ('created', 'updated')