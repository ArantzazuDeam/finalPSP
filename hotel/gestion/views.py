from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'gestion/inicio.html', {})

def habitaciones(request):
    return render(request, 'gestion/habitaciones.html', {})

def reservas(request):
    return render(request, 'gestion/reserva.html', {})
