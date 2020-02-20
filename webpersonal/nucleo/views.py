from django.shortcuts import render
from django.http import HttpResponse, Http404
import datetime
from .models import Empleado, Empresa

# Create your views here.

def fecha_actual(request):
    hoy=datetime.datetime.now().date() # Importamos datetime
    html="<html><body>Hoy es %s .</body></html>" %hoy
    return HttpResponse(html) # Importamos HttpResponse de django.http



def indice(request):
    ''' Devuelve una lista de empleados. '''
    lista_empleados=Empleado.objects.order_by('-nombre') # Importamos Empleado de .models
    context={'empleados':lista_empleados}
    return render(request, 'indice.html', context)


def empleado_nombre(request, empleado_id):
    ''' Devuelve un empleado que tenga un id concreto. '''
    try:
        emple=Empleado.objects.get(pk=empleado_id)
    
    except Empleado.DoesNotExist:
        raise Http404 ('El empleado no existe') # Importamos Http404 de django.http

    context={'emple': emple}
    return render(request, "detalles.html", context)


def listado_empresas(request):
    ''' Devuelve todas las empresas y a todos los empleados almacenados en la base de datos.'''
    empresas=Empresa.objects.all() # Importamos Empresa de .models
    empleados=Empleado.objects.all()
    context={'empresas': empresas, 'empleados': empleados}
    return render(request, "lista_e.html", context)