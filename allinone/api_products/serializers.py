from rest_framework import serializers
from .models import Product

# Serializador para el modelo Product
# Este serializador se utiliza para convertir instancias del modelo Product a formatos como JSON
# y para validar los datos antes de crear o actualizar instancias del modelo.
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        