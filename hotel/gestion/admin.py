from django.contrib import admin
from .models import Cliente, Pago, Habitacion, Factura, Detalle

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Pago)
admin.site.register(Habitacion)
admin.site.register(Factura)
admin.site.register(Detalle)