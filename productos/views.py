from django.shortcuts import render
from django.http import JsonResponse
import json 
from .models import *
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.http import HttpResponse
#Capturar multivaluedict key error
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.decorators import login_required

# Create your views here.
def agregar(request):
    print("ok, estamos en la vista agregar")
    context={}
    return render(request, 'productos/agregar.html',context)
def eliminar(request):
    print("ok, estamos en la vista eliminar")
    context={}
    return render(request, 'productos/eliminar.html',context)
def modificar(request):
    print("ok, estamos en la vista modificar")
    context={}
    return render(request, 'productos/modificar.html',context)

def buscar(request):
    print("ok, estamos en la vista buscar")
    context={}
    return render(request, 'productos/buscar.html',context)


def home(request):
    print("ok, estamos en la vista home")
    context={}
    return render(request,'productos/index.html',context)

def conocenos(request):
    print("ok, estamos en la vista conocenos")
    context={}
    return render(request,'productos/Conocenos.html',context)

def formulario(request):
    print("ok, estamos en la vista formulario")
    context={}
    return render(request,'productos/formulario.html',context)

def Ingredientes(request):
    print("ok, estamos en la vista ingredientes")
    productos = Producto.objects.filter(categoria=3)
    context={'productos': productos}
    return render(request,'productos/Ingredientes.html',context)

def Decoración(request):
    print("ok, estamos en la vista decoración")
    productos = Producto.objects.filter(categoria=2)
    context={'productos': productos}
    return render(request,'productos/Decoración.html',context)

def Utensilios(request):
    print("ok, estamos en la vista utensilios")
    
    productos = Producto.objects.filter(categoria=1)
    context={'productos': productos}
    return render(request,'productos/Utensilios.html',context)

def index(request):
    print("ok, estamos en la vista home")
    productos = Producto.objects.filter(categoria=4)
    context={'productos': productos}
    return render(request,'productos/index.html',context)

@login_required
def menu(request):
    print("ok, estamos en la vista menu")
    context={}
    return render(request,'productos/menu.html',context)

#INICIO SENTENCIAS CRUD
@login_required
def agregar_producto(request):
    print("hola  estoy en agregar_producto...")
    if request.method == 'POST':
        mi_codigo = request.POST['codigo']
        mi_categoria = request.POST['categoria']
        mi_nombre = request.POST['nombre']
        mi_precio = request.POST['precio']
        mi_foto = request.FILES.get('foto')

        if mi_codigo != "" and mi_categoria != "" and mi_nombre != "" and mi_precio != "" and mi_foto != "":

            try:
                producto = Producto()
                producto.codigo = mi_codigo
                producto.categoria = mi_categoria
                producto.nombre = mi_nombre
                producto.precio = mi_precio
                producto.imagen = mi_foto

                producto.save()

                messages.success(request, '¡Producto Agregado!')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            except producto.DoesNotExist:
                messages.error(request, 'Error, try - except error')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:

                messages.error(request, 'Error, empty data')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, 'Error, invalid method')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
#buscar para editar
@login_required
def buscar_para_editar(request):
    try:
        print("Ok, estamos en la vista buscar para editar")
        mi_codigo = request.POST['codigo']
        producto = Producto.objects.get(codigo=mi_codigo)
        context = {'producto': producto}
        messages.success(request, '¡Producto encontrado!')
        return render(request, 'productos/modificar.html', context)
        #return HttpResponseRedirect(request.META.get('HTTP_REFERER'), context)
    except Producto.DoesNotExist:
        messages.error(
            request, 'Ocurrió un error al tratar de encontrar el alumno.')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
#actualizar productos
@login_required
def actualizar_producto(request):
    print("hola  estoy en actualizar_producto...")
    if request.method == 'POST':
        mi_id = request.POST['entry_id_producto']
        mi_codigo = request.POST['codigo']
        mi_categoria = request.POST['categoria']
        mi_nombre = request.POST['nombre']
        mi_precio = request.POST['precio']
        mi_foto = request.FILES.get('foto')

        if mi_codigo != "" and mi_categoria != "" and mi_nombre != "" and mi_precio != "" and mi_foto != "":

            try:
                producto = Producto()
                producto.id_producto = mi_id
                producto.codigo = mi_codigo
                producto.categoria = mi_categoria
                producto.nombre = mi_nombre
                producto.precio = mi_precio
                producto.imagen = mi_foto

                producto.save()

                messages.success(request, '¡Producto modificado!')
                return render(request, 'productos/modificar.html')
            except producto.DoesNotExist:
                messages.error(request, 'Error, try - except error')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:

                messages.error(request, 'Error, empty data')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, 'Error, invalid method')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
#Eliminar por código
@login_required
def eliminar_por_codigo(request):
    try:
        print("Ok, estamos en la vista eliminar por codigo")
        mi_codigo = request.POST['codigo']
        producto = Producto.objects.get(codigo=mi_codigo)
        producto.delete()
        messages.success(request, '¡Producto eliminado!')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    except Producto.DoesNotExist:
        messages.error(
            request, 'Ocurrió un error al tratar de encontrar el producto.')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
#Buscar por código
@login_required
def buscar_por_codigo(request):
    try:
        print("Ok, estamos en la vista buscar por código")
        mi_codigo = request.POST['codigo']
        producto = Producto.objects.get(codigo=mi_codigo)
        context = {'producto': producto}
        messages.success(request, '¡Producto encontrado!')
        return render(request, 'productos/buscar.html', context)
    except Producto.DoesNotExist:
        messages.error(
            request, 'Ocurrió un error al tratar de encontrar el producto.')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))