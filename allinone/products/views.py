from django.shortcuts import render, redirect
from .forms import ProductForm
from django.conf import settings

# Import requests to interact with the API
import requests

API_BASE_URL = 'http://localhost:8000/api/products/'

def product_list(request):
    response = requests.get(API_BASE_URL)
    products = response.json()

    # Añade MEDIA_URL a cada imagen
    for product in products:
        if product['image']:
            product['image']
    
    return render(request, 'products/product_list.html', {'products': products})


def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            # Prepara los archivos y datos
            files = {'image': request.FILES['image']}
            data = {
                'name': form.cleaned_data['name'],
                'description': form.cleaned_data['description'],
                'price': form.cleaned_data['price'],
                'stock': form.cleaned_data['stock'],
            }
            response = requests.post(API_BASE_URL, data=data, files=files)
            if response.status_code == 201:
                return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'products/product_form.html', {'form': form})
