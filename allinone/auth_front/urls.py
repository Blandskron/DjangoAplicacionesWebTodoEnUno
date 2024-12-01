from django.urls import path
from . import views

# Definición de las rutas de la aplicación
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
