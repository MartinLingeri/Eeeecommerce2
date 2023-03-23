from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.http import JsonResponse
from register.forms import RegisterForm

from models.models import State, Cart

def index(request):
    context = {}
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Cart.objects.create(idcart=user.id, user=user.id)
            login(request, user)
            return redirect('/')
        else:
            context['form'] = form
    else:
        form = RegisterForm()
        context['form'] = form
    return render(request, 'register.html', context)


def load_states(request):
    country_id = request.GET.get('country')
    states_raw = State.objects.filter(country=country_id).values_list()
    states = [{"id_state": state[0], "name":state[1]} for state in states_raw]
    return JsonResponse(states, safe=False)
