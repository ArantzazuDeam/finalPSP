from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name=""),
    path('habitaciones', views.habitaciones, name="habitaciones"),
    path('reservas', views.reservas, name="reservas"),

]

