from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.listado_productos, name='listado'),
    path('crear/', views.crear_producto, name='crear_producto'),
]