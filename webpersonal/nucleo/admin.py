from django.contrib import admin
from .models import Empleado, Empresa
from django import forms

# Register your models here.
# Ejemplo 1
class EmpleadoAdminForm(forms.ModelForm):
    def clean_nombre(self):
        if len(self.cleaned_data['nombre'])<3:
            raise forms.ValidationError("El nombre del empleado es muy corto.")
        else:
            return self.cleaned_data['nombre']

class EmpleadoAdmin(admin.ModelAdmin):
    form=EmpleadoAdminForm

admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Empresa)


# Ejemplo 2
#class EmpleadoInline(admin.StackedInline):
#    model=Empleado

#class EmpresaAdmin(admin.ModelAdmin):
    # list_filter=['ciudad']
    # ordering=['nom']
    # list_per_page=1
    # inlines=[EmpleadoInline, ]


#admin.site.register(Empresa, EmpresaAdmin)
#admin.site.register(Empleado)
