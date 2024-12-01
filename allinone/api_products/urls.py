from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

# Crear una instancia del router predeterminado de Django Rest Framework
# Este router se encargará de generar automáticamente las URLs para las vistas del conjunto de productos (ProductViewSet)
router = DefaultRouter()

# Registrar el conjunto de vistas 'ProductViewSet' en el router con el prefijo 'products'
# Esto genera rutas RESTful como:
# - GET /products/ (lista de productos)
# - POST /products/ (crear un producto)
# - GET /products/{id}/ (detalle de un producto)
# - PUT/PATCH /products/{id}/ (actualizar un producto)
# - DELETE /products/{id}/ (eliminar un producto)
router.register(r'products', ProductViewSet, basename='product')

# Definición de las URLs de la aplicación
urlpatterns = [
    # Incluir todas las rutas generadas por el router
    path('', include(router.urls)),
]
