from django.shortcuts import render, get_object_or_404
from .models import Evento, Equipo, Empleado, Departamento

# Create your views here.
def eventos(request):
    eventos = Evento.objects.all()
    context = {'eventos': eventos}
    return render(request, 'eventos/eventos.html', context)


def evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    context = {'evento': evento}
    return render(request, 'eventos/evento.html', context)