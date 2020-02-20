from django.contrib import admin
from django.urls import path
from . import views
from .views import *
from django.contrib.auth.decorators import login_required

# Create your views here.
urlpatterns = [
    path('restaurante', views.restaurante, name="restaurante"),
    path('restaurante/menus', views.menus, name="menus"),
    path('restaurante/carta', views.platos, name="carta"),
    path('restaurante/carta/plato/<int:plato_id>', views.plato, name="plato"),
    path('restaurante/carta/addplato', login_required(crearPlato.as_view()), name="crearPlato"),
    path('restaurante/carta/editarplato/<int:pk>', login_required(editarPlato.as_view()), name="editarPlato"),
    path('restaurante/carta/delete/<int:pk>', login_required(editarPlato.as_view()), name="eliminarPlato"),
]

