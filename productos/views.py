from django.shortcuts import render

# Create your views here.


def index(request):
    print("ok, estamos en la vista index")
    context={}
    return render(request,'productos/index.html',context)

def Conocenos(request):
    print("ok, estamos en la vista conocenos")
    context={}
    return render(request,'productos/Conocenos.html',context)

def formulario(request):
    print("ok, estamos en la vista formulario")
    context={}
    return render(request,'productos/formulario.html',context)

def Ingredientes(request):
    print("ok, estamos en la vista ingredientes")
    context={}
    return render(request,'productos/Ingredientes.html',context)

def Decoración(request):
    print("ok, estamos en la vista decoración")
    context={}
    return render(request,'productos/Decoración.html',context)

def Utensilios(request):
    print("ok, estamos en la vista utensilios")
    context={}
    return render(request,'productos/Utensilios.html',context)

def menu(request):
    print("ok, estamos en la vista menu")
    context={}
    return render(request,'productos/menu.html',context)


