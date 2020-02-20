
from django import forms
from .models import Evento, Equipo, Empleado

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ('fecha', 'nombre', 'descripcion', 'lugar')
        #exclude = ['equipo']
        widgets = {
            'fecha': forms.DateTimeInput(label="fecha", required=True),
            'nombre': forms.TextInput(),
            'descripcion': forms.Textarea(),
            'lugar': forms.TextInput()            
        }