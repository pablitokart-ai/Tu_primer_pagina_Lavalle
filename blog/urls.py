<<<<<<< HEAD
from django.urls import path
from . import views
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('listado_productos')),
    path('productos/', views.listado_productos, name='listado_productos'),
    path('productos/nuevo/', views.crear_producto, name='crear_producto'),
]
=======
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]
>>>>>>> e4ab1ce1c256aac76b0ac87e71e46064d2c4c12b
