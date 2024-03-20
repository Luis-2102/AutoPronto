from django.db import models

# Create your models here.

class Servicio(models.Model):
    tit = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Modificacion")

    class Meta:
        verbose_name = "Icono Servicio"
        verbose_name_plural = "Iconos Servicios"
        ordering = ["-created"]
    def __str__(self):
        return self.tit
    
class Ventajas(models.Model):
    tit = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Modificacion")

    class Meta:
        verbose_name = "Ventaja"
        verbose_name_plural = "Ventajas"
        ordering = ["-created"]
    def __str__(self):
        return self.tit

class Entregas(models.Model):
    tit = models.CharField(verbose_name="Titulo entrega" ,max_length=100)
    description = models.TextField(verbose_name="descripción entrega" )
    img = models.ImageField(verbose_name="Imagen Entregas" , upload_to='entregas/')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Modificacion")

    class Meta:
        verbose_name = "Entrega"
        verbose_name_plural = "Entregas"
        ordering = ["-created"]
    def __str__(self):
        return self.tit
    

class Testimonios(models.Model):
    nom = models.CharField(verbose_name="Nombre", max_length=100 )
    ocu = models.CharField(verbose_name="Ocupación", max_length=100 )
    tes = models.TextField(verbose_name="Testimonio" )
    img = models.ImageField(verbose_name="Imagen Entregas" , upload_to='testimonios/')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Modificacion")

    class Meta:
        verbose_name = "Testimonio"
        verbose_name_plural = "Testimonios"
        ordering = ["-created"]
    def __str__(self):
        return self.nom
    
class Preguntas(models.Model):
    pre = models.TextField(verbose_name="Pregunta" )
    res = models.TextField(verbose_name="Respuesta" )
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Modificacion")

    class Meta:
        verbose_name = "Pregunta"
        verbose_name_plural = "Preguntas"
        ordering = ["-created"]
    def __str__(self):
        return self.pre
    
    
class Galeria(models.Model):
    nom = models.CharField(verbose_name="Nombre", max_length=100, blank=True )
    img = models.ImageField(verbose_name="Imagen Entregas" , upload_to='galeria/')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Modificacion")

    class Meta:
        verbose_name = "Galeria"
        verbose_name_plural = "Galerias"
        ordering = ["-created"]
    def __str__(self):
        return self.nom