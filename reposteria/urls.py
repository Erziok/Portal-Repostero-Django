"""reposteria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#Visualizar las imagenes
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
#Importar rest framework y quickstart
from rest_framework import routers
from quickstart import views

#Routers: Default, users, groups y producto
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'producto', views.ProductoViewSet)

urlpatterns = [
    path('productos/', include('productos.urls')),
    path('admin/', admin.site.urls),
    url(r'^accounts/', include('registration.backends.default.urls')),
    #Paths de la API
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
    path('oauth/', include('social_django.urls', namespace='social')),
    path('', include('pwa.urls')),
]
#IMAGENES
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
