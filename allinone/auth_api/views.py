from django.contrib.auth.models import User, Group
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.decorators import permission_classes

class CreateUserAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, format=None):
        username = request.data.get('username')
        password = request.data.get('password')
        role = request.data.get('role')  # Puede ser 'Admin' o 'Client'

        if not username or not password or not role:
            return Response({'error': 'Missing parameters.'}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.create_user(username=username, password=password)
            group = Group.objects.get(name=role)
            user.groups.add(group)
        except Group.DoesNotExist:
            return Response({'error': 'Role does not exist.'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'message': 'User created successfully.'}, status=status.HTTP_201_CREATED)

class CheckUserRoleAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        is_admin = request.user.groups.filter(name='Admin').exists()
        return Response({'is_admin': is_admin})