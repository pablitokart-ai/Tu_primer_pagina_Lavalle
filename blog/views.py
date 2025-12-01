<<<<<<< HEAD
from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm

def listado_productos(request):
    productos = Producto.objects.all()
    return render(request, 'blog/listado.html', {'productos': productos})

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listado_productos')
    else:
        form = ProductoForm()
    return render(request, 'blog/crear_producto.html', {'form': form})
=======
from django.shortcuts import render
from .models import Producto

def listado_productos(request):
    productos = Producto.objects.all()
    return render(request, 'blog/listado.html', {'productos': productos})
>>>>>>> e4ab1ce1c256aac76b0ac87e71e46064d2c4c12b
