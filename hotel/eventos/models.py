from django.db import models

# Create your models here.

# Modelo del Departamento
class Departamento(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    descripcion = models.TextField(max_length=400, verbose_name="Descripción")

    class Meta:
        verbose_name="departamento"
        verbose_name_plural="departamentos"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return "../"

# Modelo del Equipo
class Equipo(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    creado = models.DateTimeField(auto_now_add=True, verbose_name="Creado")

    class Meta:
        verbose_name="equipo"
        verbose_name_plural="equipos"
        ordering = ['creado']

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return "../"

# Modelo del Empleado
class Empleado(models.Model):
    dni = models.CharField(max_length=10, verbose_name="Dni")
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    apellidos = models.CharField(max_length=150, verbose_name="Apellidos")
    telefono = models.CharField(max_length=15, verbose_name="Teléfono")
    email = models.EmailField(max_length=100, unique=True, verbose_name="Email")
    salario = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Salario")
    departamento = models.ForeignKey(Departamento, null=True, on_delete=models.SET_NULL, verbose_name="Departamento")
    equipo = models.ForeignKey(Equipo, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Equipo")

    class Meta:
        verbose_name="empleado"
        verbose_name_plural="empleados"
        ordering = ['apellidos', 'nombre']

    def __str__(self):
        return self.dni +" "+ self.apellidos +", "+ self.nombre

    def get_absolute_url(self):
        return "../"

# Modelo del Evento
class Evento(models.Model):
    nombre = models.CharField(max_length=100,verbose_name="Nombre")
    descripcion = models.TextField(max_length=400, verbose_name="Descripción")
    lugar = models. CharField(max_length=100, verbose_name="Lugar")
    fecha = models.DateTimeField(verbose_name="Fecha")
    equipo = models.ForeignKey(Equipo, null=True, on_delete=models.SET_NULL,verbose_name="Equipo")
   

    class Meta:
        verbose_name = "evento"
        verbose_name_plural = "eventos"
        ordering = ['fecha', 'nombre']

    def __str__(self):
        return str(self.fecha.date()) +" "+ self.nombre 

    def get_absolute_url(self):
        return "../"