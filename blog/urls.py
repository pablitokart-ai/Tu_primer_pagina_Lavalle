from django.urls import path
from . import views
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('listado_productos')),
    path('productos/', views.listado_productos, name='listado_productos'),
    path('productos/nuevo/', views.crear_producto, name='crear_producto'),
]