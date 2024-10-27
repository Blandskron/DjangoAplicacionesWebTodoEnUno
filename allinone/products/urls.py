from django.urls import path
from . import views

urlpatterns = [
    path('products/public/', views.product_list_public, name='product_list_public'),
    path('products/client/', views.product_list_client, name='product_list_client'),
    path('products/admin/', views.product_list_admin, name='product_list_admin'),
    path('create/', views.product_create, name='product_create'),
    path('update/<int:pk>/', views.product_update, name='product_update'),
    path('delete/<int:pk>/', views.product_delete, name='product_delete'),
]
