from django.contrib import admin
from .models import Categoria, TipoMenu, Plato

# Register your models here.
admin.site.register(Categoria)
admin.site.register(TipoMenu)
admin.site.register(Plato)