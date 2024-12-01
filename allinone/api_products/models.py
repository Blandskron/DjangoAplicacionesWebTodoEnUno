from django.db import models

# Modelo que representa un producto en el sistema
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    # Representación en cadena del objeto que devuelve el nombre del producto
    def __str__(self):
        return self.name
    