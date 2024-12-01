from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# ViewSet para manejar las operaciones CRUD del modelo Product
# El ViewSet combina las vistas y la lógica de controladores para exponer
# las operaciones de lista, creación, actualización y eliminación a través de la API.
@method_decorator(csrf_exempt, name='dispatch')
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    