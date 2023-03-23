from django.urls import path
from mis_compras import views

urlpatterns = [
    path("", views.index),
]
