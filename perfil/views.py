from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from models.models import Countries, State

from .forms import UpdateCustomUserData, UpdateCustomUserPassword

def index(request):
    if not request.user.is_authenticated:
        return redirect('/login')

    country = Countries.objects.get(idcountries=request.user.country).name
    state = State.objects.get(idstate=request.user.state).name
    return render(request, 'perfil.html', {"country": country, "state": state})

def cambio_nombre_y_pais(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    
    context={}

    if request.POST:
        form = UpdateCustomUserData(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Datos actualizados correctamente')
            return redirect('/perfil/')
    else:
        form = UpdateCustomUserData(
            initial={
                'nombre': request.user.nombre,
                'country': request.user.country,
                'state': request.user.state
            }
        )
    context['form'] = form
    return render(request, 'change_name.html', context)

def cambio_contrasenia(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    
    context = {}

    if request.POST:
        form = UpdateCustomUserPassword(request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Contraseña actualizada correctamente')
            return redirect('/perfil/')
    else:
        form = UpdateCustomUserPassword(user=request.user)
    context['form'] = form
    return render(request, 'change_password.html', context)