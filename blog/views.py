from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm

def listado_productos(request):
    productos = Producto.objects.all()
    return render(request, 'blog/listado.html', {'productos': productos})

def crear_producto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listado')
    else:
        form = ProductoForm()
    return render(request, 'blog/crear_producto.html', {'form': form})