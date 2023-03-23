from django.urls import path
from register import views

urlpatterns = [
    path("", views.index),
    path("load_states/", views.load_states, name="load_states")
]
