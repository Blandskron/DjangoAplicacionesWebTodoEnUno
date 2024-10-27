from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CreateUserAPIView, CheckUserRoleAPIView

router = DefaultRouter()
router.register(r'create_user', CreateUserAPIView, basename='create_user')
router.register(r'check_user_role', CheckUserRoleAPIView, basename='check_user_role')

# Se incluyen las rutas del router
urlpatterns = [
    path('', include(router.urls)),
]
