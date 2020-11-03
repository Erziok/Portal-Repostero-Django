from django.db import models

# Create your models here.

class Producto(models.Model):
    id_producto = models.AutoField(db_column='id_producto', primary_key=True)
    codigo = models.IntegerField(blank=False, unique=False, null=True)
    categoria = models.IntegerField(blank=True, null=False)
    nombre = models.CharField(max_length=200)
    precio = models.IntegerField()
    imagen = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.nombre
    #funcion para evitar errores si los productos no tienen foto
    @property
    def imagenURL(self):
        try:
            url = self.imagen.url
        except:
            url = ''
        return url