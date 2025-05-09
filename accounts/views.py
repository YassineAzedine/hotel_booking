from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if password1 != password2:
            return render(request, 'accounts/register.html', {'error': 'Les mots de passe ne correspondent pas.'})
        
        if User.objects.filter(username=username).exists():
            return render(request, 'accounts/register.html', {'error': 'Ce nom d’utilisateur existe déjà.'})
        
        user = User.objects.create_user(username=username, password=password1)
        login(request, user)
        return redirect('home')  # Redirige vers l'accueil après l'inscription

    return render(request, 'accounts/register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Remplace 'home' par l'URL de ton choix
        else:
            return render(request, 'accounts/login.html', {'error': 'Identifiants invalides.'})
    
    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')
