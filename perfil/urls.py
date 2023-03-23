from django.urls import path
from perfil import views

urlpatterns = [
    path("", views.index),
    path("cambio_nombre_y_pais/", views.cambio_nombre_y_pais),
    path("cambio_contrasenia/", views.cambio_contrasenia),
]
