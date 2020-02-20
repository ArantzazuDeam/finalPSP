from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from .models import Plato, TipoMenu, Categoria
from .forms import PlatoForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

# Create your views here.
def restaurante(request):
    return render(request, 'restaurante/restaurante.html', {})

def menus(request):
    ''' Lista todos los mensus con los platos que incluyen.'''
    menus = TipoMenu.objects.all()
    platos = Plato.objects.all()
    context = {'menus': menus, 'platos': platos}
    return render(request, 'restaurante/menus.html', context)

def platos(request):
    ''' Lista todos los platos organizados por categorías.'''
    categorias = Categoria.objects.all()
    platos = Plato.objects.all()
    context = {'categorias': categorias, 'platos': platos}
    return render(request, 'restaurante/platos.html', context)

#CRUD de Plato
def plato(request, plato_id):
    ''' Muestra los detalles de un plato. '''
    plato = get_object_or_404(Plato, id=plato_id)
    context = {'plato': plato}
    return render(request, 'restaurante/plato.html', context)

class crearPlato(CreateView):
    form_class=PlatoForm
    model=Plato
    success_url=reverse_lazy('carta')

class editarPlato(UpdateView):
    model=Plato
    form_class=PlatoForm    


def eliminarPlato():
    '''Elimina un plato'''
    pass

class eliminarPlato(DeleteView):
    model=Plato
    success_url=reverse_lazy('carta')
    template_name_suffix = '_confirm_delete'    