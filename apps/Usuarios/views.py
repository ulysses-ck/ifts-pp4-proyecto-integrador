from pyexpat.errors import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from apps.Usuarios.forms import LoginForm, RegisterForm
from apps.Usuarios.models import User
from django.contrib import messages

# Create your views here.
# Vista de registro
@csrf_protect
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el usuario y el UserAdmin asociado
            return redirect('user:login')  # Redirige a la página de inicio o a donde desees
    else:
        form = RegisterForm()
    
    return render(request, 'register.html', {'form': form})




# Vista de login
@csrf_protect
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request,username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login exitoso.")
                return redirect('turn:home_turn')
            else:
                messages.error(request, "Credenciales incorrectas.")
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

# Vista de logout
@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "Has cerrado sesión correctamente.")
    return redirect('user:login')


# Vista protegida, requiere login
@login_required
def home_view(request):
    return render(request, "home_turn.html", {"user": request.user})
