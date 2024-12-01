from django.urls import path
from .views import CreateUserAPIView, CheckUserRoleAPIView

# Definición de las rutas de la API relacionadas con la gestión de usuarios
urlpatterns = [
    path('create_user/', CreateUserAPIView.as_view(), name='create_user'),
    path('check_user_role/', CheckUserRoleAPIView.as_view(), name='check_user_role'),
]
