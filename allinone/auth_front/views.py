from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required

# Vista para el registro de usuarios
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            role = request.POST.get('role')
            if role:
                try:
                    group = Group.objects.get(name=role)
                    user.groups.add(group)
                    messages.success(request, 'Registration successful.')
                    return redirect('login')
                except Group.DoesNotExist:
                    user.delete()  # Eliminar el usuario si el rol no existe
                    messages.error(request, 'The specified role does not exist. Please choose a valid role.')
            else:
                messages.error(request, 'Role not selected. Please choose a valid role.')
    else:
        form = UserCreationForm()

    return render(request, 'auth_front/register.html', {'form': form})

# Vista para el inicio de sesión
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Welcome {user.username}!')

            # Redireccionar basándose en el grupo del usuario
            if user.groups.filter(name='Admin').exists():
                return redirect('product_list_admin')
            elif user.groups.filter(name='Client').exists():
                return redirect('product_list_client')
            else:
                return redirect('product_list_public')
        else:
            messages.error(request, 'Invalid username or password.')

    else:
        form = AuthenticationForm()

    return render(request, 'auth_front/login.html', {'form': form})

# Vista para el cierre de sesión (restringida a usuarios autenticados)
@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully.')
    return redirect('login')