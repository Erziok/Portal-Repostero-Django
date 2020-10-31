from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('Conocenos', views.Conocenos, name='Conocenos'),
    path('formulario', views.formulario, name='formulario'),
    path('Ingredientes', views.Ingredientes, name='Ingredientes'),
    path('Decoración', views.Decoración, name='Decoración'),
    path('Utensilios', views.Utensilios, name='Utensilios'),
    path('menu', views.menu, name='menu'),
]