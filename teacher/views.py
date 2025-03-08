from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login(request):
    return render(request, "login.html")

def admin_login(request):
    if request.user.is_authenticated:  
        return redirect('admin_dashboard')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_superuser:
            messages.error(request, 'Succes')
            return redirect('login')  # Redirect to the login view
        else:
            messages.error(request, 'Invalid credentials or not an admin.')

    return render(request, 'login.html')


    return redirect('admin_login')