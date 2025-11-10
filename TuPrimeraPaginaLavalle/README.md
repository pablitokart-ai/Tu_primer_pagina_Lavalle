# TuPrimeraPaginaLavalle

Proyecto Django mínimo entregable para la consigna: un modelo, una vista que liste los objetos, README, .gitignore y requirements.txt.

## Cómo usar

1. Crear y activar entorno virtual:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   # o
   source venv/bin/activate  # Linux / macOS
   ```
2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Aplicar migraciones:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
4. Crear superusuario (opcional, para admin):
   ```bash
   python manage.py createsuperuser
   ```
5. Ejecutar servidor:
   ```bash
   python manage.py runserver
   ```
6. Abrir en el navegador:
   `http://127.0.0.1:8000/` para ver el listado de productos.

## Contenido

- app `blog` con un modelo `Producto`
- vista `listado_productos` mostrando los objetos
- admin habilitado para cargar productos desde el panel
