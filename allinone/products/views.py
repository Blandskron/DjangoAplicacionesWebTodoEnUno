from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import ProductForm
import requests
from django.contrib import messages
import logging

# URL base para interactuar con la API de productos
API_BASE_URL = 'http://127.0.0.1:8000/api-products/products/'

def is_admin(user):
    return user.is_authenticated and user.groups.filter(name='Admin').exists()

def is_client(user):
    return user.is_authenticated and user.groups.filter(name='Client').exists()

def handle_api_errors(response):
    try:
        data = response.json()
    except ValueError:
        data = {'error': 'Response content is not valid JSON'}
    return data

def get_common_context(request):
    return {
        'is_admin': is_admin(request.user),
        'is_client': is_client(request.user),
    }

logger = logging.getLogger(__name__)

def product_list_public(request):
    if request.user.is_authenticated:
        if is_admin(request.user):
            logger.debug("Admin attempting to access public list, redirecting to admin list.")
            return redirect('product_list_admin')
        elif is_client(request.user):
            logger.debug("Client attempting to access public list, redirecting to client list.")
            return redirect('product_list_client')
    
    try:
        response = requests.get(API_BASE_URL)
        response.raise_for_status()
        products = response.json()
    except requests.exceptions.RequestException as e:
        messages.error(request, f"Failed to fetch products: {e}")
        products = []

    context = {'products': products}
    context.update(get_common_context(request))
    return render(request, 'products/product_list_public.html', context)

@login_required
@user_passes_test(is_client)
def product_list_client(request):
    try:
        response = requests.get(API_BASE_URL)
        response.raise_for_status()
        products = response.json()
    except requests.exceptions.RequestException as e:
        messages.error(request, f"Failed to fetch products: {e}")
        products = []

    context = {'products': products}
    context.update(get_common_context(request))
    return render(request, 'products/product_list_client.html', context)

@login_required
@user_passes_test(is_admin)
def product_list_admin(request):
    try:
        response = requests.get(API_BASE_URL)
        response.raise_for_status()
        products = response.json()
    except requests.exceptions.RequestException as e:
        messages.error(request, f"Failed to fetch products: {e}")
        products = []

    context = {'products': products}
    context.update(get_common_context(request))
    return render(request, 'products/product_list_admin.html', context)

@login_required
@user_passes_test(is_admin)
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            files, data = prepare_product_data(form, request)
            try:
                response = requests.post(API_BASE_URL, data=data, files=files)
                response.raise_for_status()
                return redirect('product_list_admin')
            except requests.exceptions.RequestException as e:
                messages.error(request, f"Failed to create product: {e}")
    else:
        form = ProductForm()
    return render(request, 'products/product_form.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def product_update(request, pk):
    url = f"{API_BASE_URL}{pk}/"
    try:
        response = requests.get(url)
        response.raise_for_status()
        product = response.json()
    except requests.exceptions.RequestException as e:
        messages.error(request, f"Failed to fetch product: {e}")
        return redirect('product_list_admin')

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            files, data = prepare_product_data(form, request)
            try:
                response = requests.put(url, data=data, files=files)
                response.raise_for_status()
                return redirect('product_list_admin')
            except requests.exceptions.RequestException as e:
                messages.error(request, f"Failed to update product: {e}")
    else:
        form = ProductForm(initial=product)
    return render(request, 'products/product_form.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def product_delete(request, pk):
    url = f"{API_BASE_URL}{pk}/"
    if request.method == 'POST':
        try:
            response = requests.delete(url)
            response.raise_for_status()
            return redirect('product_list_admin')
        except requests.exceptions.RequestException as e:
            messages.error(request, f"Failed to delete product: {e}")
    else:
        try:
            response = requests.get(url)
            response.raise_for_status()
            product = response.json()
        except requests.exceptions.RequestException as e:
            messages.error(request, f"Failed to fetch product: {e}")
            return redirect('product_list_admin')
    return render(request, 'products/product_confirm_delete.html', {'product': product})

def prepare_product_data(form, request):
    files = {'image': request.FILES['image']} if request.FILES else None
    data = {
        'name': form.cleaned_data['name'],
        'description': form.cleaned_data['description'],
        'price': form.cleaned_data['price'],
        'stock': form.cleaned_data['stock'],
    }
    return files, data