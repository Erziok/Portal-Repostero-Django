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
    #vistas crud
    path('agregar', views.agregar, name='agregar'),
    path('eliminar', views.eliminar, name='eliminar'),
    path('modificar', views.modificar, name='modificar'),
    path('buscar', views.buscar, name='buscar'),
    #CRUD
    path('agregar_producto', views.agregar_producto, name='agregar_producto'),
    path('buscar_para_editar', views.buscar_para_editar, name='buscar_para_editar'),
    path('actualizar_producto', views.actualizar_producto, name='actualizar_producto'),
    path('eliminar_por_codigo', views.eliminar_por_codigo, name='eliminar_por_codigo'),
    path('buscar_por_codigo', views.buscar_por_codigo, name='buscar_por_codigo'),

]