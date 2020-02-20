from django.db import models

# Create your models here.

# Modelo de Cliente
class Cliente(models.Model):
    dni = models.CharField(max_length=10, verbose_name="Dni")
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    apellidos = models.CharField(max_length=150, verbose_name="Apellidos")
    telefono = models.CharField(max_length=15, verbose_name="Teléfono")
    email = models.EmailField(max_length=100, unique=True, verbose_name="Email")
    
    class Meta:
        verbose_name="cliente"
        verbose_name_plural="clientes"
        ordering = ['apellidos', 'nombre']

    def __str__(self):
        return self.dni +": "+ self.apellidos +", "+ self.nombre

    def get_absolute_url(self):
        return '../'


# Modelo de los tipos de Pago
class Pago(models.Model):
    tipo = models.CharField(max_length=10, verbose_name="Tipo de pago")
    descripcion = models.TextField(max_length=400, verbose_name="Descripción")

    class Meta:
        verbose_name="modo de pago"
        verbose_name_plural="modos de pago"
        ordering =['tipo']

    def __str__(self):
        return self.tipo

    def get_absolute_url(self):
        return '../'

# Modelo de Tipo de Habitación
class Habitacion(models.Model):
    nombre = models.CharField(max_length=20, unique=True, verbose_name="Nombre")
    descripcion = models.TextField(max_length=400, verbose_name="Descripción")
    precio_noche = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Precio por noche") # una habitacón puede costar como máximo 999,99
    foto = models.ImageField(upload_to="fotos/habitaciones/", max_length=400 ,verbose_name="Imagen de la habitación")

    class Meta:
        verbose_name="habitación"
        verbose_name_plural="habitaciones"
        ordering =['nombre']

    def __str__(self):
        return self.nombre + " " + self.precio +" €"

    def get_absolute_url(self):
        return '../'

# Modelo de Factura de la reserva
class Factura(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="Cliente") # Si el cliente queda eliminado del sistema no guardaremos las facutras asociadas al mismo
    fecha_inicio = models.DateField(verbose_name="Fecha de entrada")
    fecha_fin = models.DateField(verbose_name="Fecha de salida")
    num_personas = models.PositiveSmallIntegerField(verbose_name="Número de personas")
    num_habitaciones = models.PositiveSmallIntegerField(verbose_name="Número de habitaciones")
    precio_total = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Precio total") # una habitacón puede costar como máximo 99999,99
    modo_pago = models.ForeignKey(Pago, null=True, on_delete=models.SET_NULL, verbose_name="Modo de pago") # Si por alguna razón los métodos de pago cambian o se eliminan de la tabla pero el cliente ya se ha alojado, no perdemos la factura
    pagado = models.BooleanField(default=False ,verbose_name="Pagado")

    class Meta:
        verbose_name="factura"
        verbose_name_plural="facturas"
        ordering =['fecha_inicio']

    def __str__(self):
        return self.cliente.nombre + " -> Entrada: " +self.fecha_inicio+ " ; Salida: " +self.fecha_fin

    def get_absolute_url(self):
        return '../'

# Modelo de las Lineas de Detalle de las facturas de las reservas.
class Detalle(models.Model):
    reserva = models.ForeignKey(Factura, on_delete=models.CASCADE, verbose_name="Factura")
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE, verbose_name="Habitación")
    num_noches = models.PositiveIntegerField(verbose_name="Número de noches")
    precio_hab_noches = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Precio de la habitación por num_noches")

    class Meta:
        verbose_name="linea detallada de factura"
        verbose_name_plural="linea detalladas de factura"

    def __str__(self):
        return self.habitacion.nombre + " ->Precio por noche: " +self.habitacion.precio_noche+ " ; Noches: " +self.num_noches+ " ; Precio(total de noches): " +self.precio_hab_noches
    
    def get_absolute_url(self):
        return '../'