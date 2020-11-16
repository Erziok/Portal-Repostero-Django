from django.contrib.auth.models import User, Group
from rest_framework import serializers
#Importar el modelo Producto
from productos.models import Producto

#Serializer de los usuarios
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

#Serializer de los grupos
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

#Serializer de los productos
class ProductoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producto
        fields = ['id_producto', 'codigo', 'categoria', 'nombre', 'precio', 'imagen']