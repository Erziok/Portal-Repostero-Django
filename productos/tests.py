from django.test import TestCase
import unittest
from .models import *
from django.db.models import Q
# Create your tests here.

class testProducto(unittest.TestCase):

    def test_verif_cod(self):
        #__gt es oara decir mayor que
        #__lt es para decir menor que
        #__gte es oara decir mayor o igual que
        #__lte es para decir menor o igual que
        #usar ~Q, = es para decir que sea distinto de (!=)
        productoBueno = Producto.objects.filter(codigo__gte=1).count()
        
        producto = Producto.objects.count()
        
        self.assertEqual(productoBueno, producto)

    def test_creacion_producto(self):
        producto = Producto.objects.create( codigo = 6,
                                            categoria = 2,
                                            nombre = 'lechuga',
                                            precio = 1022,
                                            imagen = '')

        producto.save()
        self.assertTrue(producto, True)
    

