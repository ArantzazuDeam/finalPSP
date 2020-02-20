from django.shortcuts import render

# Create your views here.
def jugadores(request):
    jugadores=Jugador.objects.all()
    return render(request, "jugadores.html", {'posts':posts})
