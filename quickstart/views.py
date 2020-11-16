from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
#Importar el modelo del producto
from productos.models import Producto
#Importar los serializers de User, Group y Producto
from quickstart.serializers import UserSerializer, GroupSerializer, ProductoSerializer

#Vista de los usuarios
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined') #Query para obtener todos los objetos del modelo User, ordenado por la fecha de registro
    serializer_class = UserSerializer #Serializer
    permission_classes = [permissions.IsAuthenticated]

#Vista de los grupos
class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all() #Query para obtener todos los objetos del modelo Group
    serializer_class = GroupSerializer #Serializer
    permission_classes = [permissions.IsAuthenticated]

#Vista de los productos
class ProductoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Producto.objects.all() #Query para obtener todos los objetos del modelo Producto
    serializer_class = ProductoSerializer #Serializer
    permission_classes = [permissions.IsAuthenticated] 