# TuPrimeraPaginaLavalle

Proyecto Django mínimo entregable para la consigna:  
- 1 modelo  
- 1 vista que liste objetos  
- herencia de plantillas  
- README  
- .gitignore  
- requirements.txt  

## 🔧 Cómo usar el proyecto

### 1. Crear y activar el entorno virtual
```bash
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Linux / macOS
```

### 2. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 3. Aplicar migraciones
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Crear superusuario (opcional)
```bash
python manage.py createsuperuser
```

### 5. Ejecutar el servidor
```bash
python manage.py runserver
```

### 6. Abrir en el navegador
```
http://127.0.0.1:8000/
```

---

## ▶️ Orden para probar el proyecto (lo que pide la consigna)

1. **Ingresar a la ruta principal**  
   `http://127.0.0.1:8000/`  
   Esto muestra la **vista listando los productos**.

2. **(Opcional)** Ingresar al panel de administración  
   `http://127.0.0.1:8000/admin/`  
   Ahí se pueden **crear, editar o eliminar productos**.

3. Volver a la página principal y refrescar:  
   Se verá automáticamente el listado actualizado.

---

## 📂 ¿Dónde están las funcionalidades?

### **Modelo**
`blog/models.py`  
- `Producto`: nombre, descripción, precio.

### **Vista**
`blog/views.py`  
- `listado_productos`: retorna la lista de productos a la plantilla.

### **URL principal**
`TuPrimeraPaginaLavalle/urls.py` → incluye las URLs del blog.

### **URLs del blog**
`blog/urls.py`  
- Ruta `/` → muestra el listado de productos.

### **Templates**
`blog/templates/`  
- `base.html` → plantilla base  
- `listado.html` → muestra los productos  

---
