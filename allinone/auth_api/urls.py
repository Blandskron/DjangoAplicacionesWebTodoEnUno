from django.urls import path
from .views import CreateUserAPIView, CheckUserRoleAPIView

urlpatterns = [
    path('create_user/', CreateUserAPIView.as_view(), name='create_user'),
    path('check_user_role/', CheckUserRoleAPIView.as_view(), name='check_user_role'),
]
