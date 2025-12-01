TuPrimeraPaginaLavalle

Proyecto Django para la entrega del curso, cumpliendo con los requisitos:

✔ 1 modelo

✔ 1 vista que liste objetos

✔ formularios para crear productos

✔ herencia de plantillas

✔ README

✔ .gitignore

✔ requirements.txt

✔ rutas funcionando

🚀 Cómo usar el proyecto
1. Crear y activar el entorno virtual
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Linux / macOS

2. Instalar dependencias
pip install -r requirements.txt

3. Aplicar migraciones
python manage.py makemigrations
python manage.py migrate

4. Crear superusuario (opcional)
python manage.py createsuperuser

5. Ejecutar el servidor
python manage.py runserver


Luego abrir en el navegador:

http://127.0.0.1:8000/

▶️ Cómo probar el proyecto (lo que pide la consigna)
1. Listado de productos

Ir a:

http://127.0.0.1:8000/productos/


Muestra el listado completo de productos cargados en la base.

2. Formulario para crear productos

Ir a:

http://127.0.0.1:8000/productos/nuevo/


Ahí se puede cargar un nuevo producto usando el formulario.

3. Panel de administración (opcional)
http://127.0.0.1:8000/admin/


Desde allí se pueden crear/editar/eliminar productos desde el admin de Django.

📌 Estructura del proyecto
TuPrimeraPaginaLavalle/
│
├── blog/
│   ├── migrations/
│   ├── templates/
│   │   ├── base.html
│   │   ├── listado.html
│   │   └── crear_producto.html
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── TuPrimeraPaginaLavalle/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
└── README.md

📂 Detalle de las funcionalidades
Modelo — blog/models.py
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()

Formulario — blog/forms.py

Formulario basado en ModelForm para crear productos.

Vistas — blog/views.py

listado_productos: muestra todos los productos.

crear_producto: permite crear un producto desde un formulario.

URLs — blog/urls.py
productos/          → listado de productos
productos/nuevo/    → formulario de creación

Plantillas (templates)

base.html → estructura general

listado.html → muestra productos

crear_producto.html → formulario para cargar productos

✔ Entrega lista

Este proyecto cumple todo lo solicitado por el profesor, incluyendo:

modelo

vista

formulario

listado

templates

herencia

README

requirements

git correctamente configurado