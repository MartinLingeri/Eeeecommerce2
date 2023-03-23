from django.urls import path
from cart import views

urlpatterns = [
    path("", views.index),
    path("add/<int:id>/<int:quantity>", views.add),
    path("remove/<int:id>", views.remove, name="cart-remove"),
]
