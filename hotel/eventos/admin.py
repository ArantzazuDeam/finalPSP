from django.contrib import admin
from .models import Departamento, Equipo, Empleado, Evento

# Register your models here.
class EventoInline(admin.StackedInline):
    model=Evento

class EquipoAdmin(admin.ModelAdmin):
    min_num=1
    list_filter=['nombre']
    ordering=['creado']    
    search_fields=['nombre']
    inlines = [EventoInline,]

admin.site.register(Departamento)
admin.site.register(Empleado)
admin.site.register(Equipo, EquipoAdmin)
admin.site.register(Evento)