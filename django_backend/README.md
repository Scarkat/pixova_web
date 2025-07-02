# Pixova Web - Backend Django

Backend para el sistema de administración de contenido de Pixova Web.

## Características

- **Django Admin**: Interfaz de administración para gestionar contenido
- **Django REST Framework**: APIs para servir contenido dinámicamente
- **Modelos**: Multimedia, Clientes, Newsletter, Servicios, Contacto
- **CORS**: Configurado para permitir peticiones desde el frontend

## Instalación

1. **Clonar el repositorio**
```bash
git clone <repository-url>
cd pixova_web/django_backend
```

2. **Crear entorno virtual**
```bash
python -m venv venv
```

3. **Activar entorno virtual**
```bash
# Windows
.\venv\Scripts\Activate.ps1

# Linux/Mac
source venv/bin/activate
```

4. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

5. **Configurar base de datos**
```bash
python manage.py makemigrations
python manage.py migrate
```

6. **Crear superusuario**
```bash
python manage.py createsuperuser
```

7. **Ejecutar servidor**
```bash
python manage.py runserver
```

## Uso

### Acceso al Admin
- URL: http://localhost:8000/admin/
- Usar las credenciales del superusuario creado

### APIs Disponibles

- **Multimedia**: `/api/multimedia/`
- **Clientes**: `/api/clientes/`
- **Newsletter**: `/api/newsletter/`
- **Servicios**: `/api/servicios/`
- **Contacto**: `/api/contacto/`

### Endpoints Especiales

- **Suscribirse al newsletter**: `POST /api/newsletter/subscribe/`
- **Información de contacto**: `GET /api/contacto/info/`

## Estructura del Proyecto

```
django_backend/
├── content/                 # Aplicación principal
│   ├── models.py           # Modelos de datos
│   ├── admin.py            # Configuración del admin
│   ├── serializers.py      # Serializers para APIs
│   ├── views.py            # Vistas de las APIs
│   └── urls.py             # URLs de la aplicación
├── pixova_web/             # Configuración del proyecto
│   ├── settings.py         # Configuración principal
│   └── urls.py             # URLs principales
├── media/                  # Archivos subidos (imágenes)
├── static/                 # Archivos estáticos
├── manage.py               # Script de gestión
└── requirements.txt        # Dependencias
```

## Modelos

### MultimediaItem
- Título, imagen, descripción
- Orden de visualización
- Estado activo/inactivo

### Cliente
- Nombre, logo, sitio web
- Orden de visualización
- Estado activo/inactivo

### Newsletter
- Email del suscriptor
- Estado de suscripción
- Fechas de suscripción/desuscripción

### Servicio
- Título, descripción, imagen
- Orden de visualización
- Estado activo/inactivo

### Contacto
- Información de contacto de la empresa
- Horarios de atención
- Solo una instancia permitida

## Desarrollo

### Agregar nuevos modelos
1. Definir el modelo en `content/models.py`
2. Crear migración: `python manage.py makemigrations`
3. Aplicar migración: `python manage.py migrate`
4. Configurar admin en `content/admin.py`
5. Crear serializer en `content/serializers.py`
6. Crear vista en `content/views.py`
7. Agregar URL en `content/urls.py`

### Personalizar el Admin
- Editar `content/admin.py`
- Usar decoradores `@admin.register()`
- Personalizar `list_display`, `list_filter`, etc.

## Producción

### Configuraciones importantes
- Cambiar `DEBUG = False`
- Configurar `ALLOWED_HOSTS`
- Usar base de datos PostgreSQL
- Configurar `STATIC_ROOT` y `MEDIA_ROOT`
- Configurar CORS apropiadamente
- Usar variables de entorno para `SECRET_KEY`

### Comandos útiles
```bash
# Recolectar archivos estáticos
python manage.py collectstatic

# Crear backup de la base de datos
python manage.py dumpdata > backup.json

# Restaurar backup
python manage.py loaddata backup.json
``` 