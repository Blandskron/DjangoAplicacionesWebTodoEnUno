# **Gestión de Productos - Django**

Este proyecto es un sistema de gestión de productos construido con Django, que incluye autenticación por roles (Admin y Cliente) y la integración con una API externa para gestionar productos.

---

## **Índice**

1. [Requisitos previos](#requisitos-previos)
2. [Instalación](#instalación)
   - [Clonar el repositorio](#clonar-el-repositorio)
   - [Configurar el entorno virtual](#configurar-el-entorno-virtual)
   - [Instalar dependencias](#instalar-dependencias)
3. [Configuración del proyecto](#configuración-del-proyecto)
4. [Ejecutar el proyecto](#ejecutar-el-proyecto)
5. [Despliegue en producción](#despliegue-en-producción)
6. [Uso](#uso)
7. [Contribuciones](#contribuciones)
8. [Licencia](#licencia)

---

## **Requisitos previos**

Asegúrate de tener instaladas las siguientes herramientas en tu sistema:

- Python 3.8 o superior.
- `pip` para gestionar paquetes de Python.
- `virtualenv` para crear entornos virtuales.
- Base de datos SQLite (incluida por defecto en Django) o PostgreSQL si prefieres usar una base de datos más robusta.

---

## **Instalación**

### **Clonar el repositorio**

```bash
git clone https://github.com/tu_usuario/tu_repositorio.git
cd tu_repositorio
```

### **Configurar el entorno virtual**

1. Crear el entorno virtual:

   ```bash
   python -m venv env
   ```

2. Activar el entorno virtual:

   - **Windows**:
     ```bash
     .\env\Scripts\activate
     ```
   - **Linux/Mac**:
     ```bash
     source env/bin/activate
     ```

### **Instalar dependencias**

Puedes instalar las librerías necesarias de dos formas:

#### **Instalar cada librería manualmente**
Ejecuta los siguientes comandos para instalar las librerías principales utilizadas en el proyecto:

```bash
pip install django
pip install djangorestframework
pip install requests
pip install drf-spectacular
```

#### **Instalar dependencias desde `requirements.txt`**

Si prefieres instalar todas las dependencias de una sola vez:

```bash
pip install -r requirements.txt
```

---

## **Configuración del proyecto**

### **Configurar la base de datos**

El proyecto está configurado para usar SQLite por defecto. Si deseas usar PostgreSQL:

1. Instala el conector de PostgreSQL:

   ```bash
   pip install psycopg2-binary
   ```

2. Modifica el archivo `settings.py` para conectar con tu base de datos PostgreSQL:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'tu_base_de_datos',
           'USER': 'tu_usuario',
           'PASSWORD': 'tu_contraseña',
           'HOST': '127.0.0.1',
           'PORT': '5432',
       }
   }
   ```

3. Aplica las migraciones:

   ```bash
   python manage.py migrate
   ```

---

## **Ejecutar el proyecto**

1. Crear las migraciones iniciales:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

2. Crear un usuario administrador:

   ```bash
   python manage.py createsuperuser
   ```

   Ingresa los datos requeridos para el usuario administrador.

3. Correr el servidor de desarrollo:

   ```bash
   python manage.py runserver
   ```

   El servidor estará disponible en: [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## **Despliegue en producción**

### **Usando Gunicorn y Nginx**

1. Instalar Gunicorn:

   ```bash
   pip install gunicorn
   ```

2. Ejecutar Gunicorn:

   ```bash
   gunicorn myproject.wsgi:application --bind 0.0.0.0:8000
   ```

3. Configurar un servidor web como **Nginx** para manejar las solicitudes entrantes y servir archivos estáticos.

4. Recuerda configurar correctamente el archivo `.env` en producción para mantener seguras las credenciales.

---

## **Uso**

1. **Documentación API**:
   - Swagger: [http://127.0.0.1:8000/schema/swagger-ui/](http://127.0.0.1:8000/schema/swagger-ui/)
   - Redoc: [http://127.0.0.1:8000/schema/redoc/](http://127.0.0.1:8000/schema/redoc/)

2. **Roles disponibles**:
   - **Admin**: Acceso completo a la gestión de productos.
   - **Client**: Acceso restringido a la lista de productos específicos.

3. **Vistas principales**:
   - Lista pública: `/public/`
   - Lista para clientes: `/client/`
   - Gestión para administradores: `/admin/`

---

## **Contribuciones**

Si deseas contribuir al proyecto, sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una rama para tu funcionalidad o corrección:
   ```bash
   git checkout -b feature/nueva_funcionalidad
   ```
3. Realiza tus cambios y sube tu rama:
   ```bash
   git push origin feature/nueva_funcionalidad
   ```
4. Crea un Pull Request en el repositorio principal.

---

## **Licencia**

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
