from django.db import models

# Create your models here.

class Producto(models.Model):
    id_producto         = models.AutoField(db_column='id_producto', primary_key=True)
    nombre              = models.CharField(max_length=20, blank=True, null=True)
    descripcion         = models.CharField(max_length=20, blank=True, null=True)
    categoria           = models.CharField(max_length=20, blank=True, null=True)
    precio              = models.IntegerField(blank=True, null=True)
    foto                = models.ImageField(upload_to='fotos', blank=True, null=True)
    activo              = models.IntegerField(blank=True, null=True)
