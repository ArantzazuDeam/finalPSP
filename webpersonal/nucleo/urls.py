from django.contrib import admin
from django.urls import path
from nucleo import views


urlpatterns=[
    path('fecha', views.fecha_actual, name="fecha"),
    path('', views.indice, name="indice"),
    path('detalle/<int:empleado_id>', views.empleado_nombre, name="empleado_nombre"),
    path('Empresas', views.listado_empresas, name="listado_e")
]