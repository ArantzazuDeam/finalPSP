from django import forms
from .models import *

class PlatoForm(forms.ModelForm):
    class Meta:
        model = Plato
        fields='__all__'