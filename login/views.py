from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from login.forms import LoginForm


def index(request):
    context = {}
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            nombre = request.POST['nombre']
            password = request.POST['password']
            user = authenticate(request, nombre=nombre, password=password)
            if user:
                login(request, user)
                return redirect('/')
        else:
            context['form'] = form
    else:
        form = LoginForm()
    context['form'] = form
    return render(request, 'login.html', context)
