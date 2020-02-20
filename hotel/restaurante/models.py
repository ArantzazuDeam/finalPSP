from django.db import models

# Create your models here.

# Modelo de las Categorías de los platos
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    descripcion = models.TextField(max_length=400, verbose_name="Descripción")

    class Meta:
        verbose_name="categoría"
        verbose_name_plural="categorías"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return '../'

# Modelo del Tipo de Menu
class TipoMenu(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    descripcion_dias = models.TextField(max_length=400, verbose_name="Horarios")
    hora_inicio = models.TimeField(verbose_name="Hora de inicio")
    hora_fin = models.TimeField(verbose_name="Hora de finalización")
    precio = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Precio del menú")

    class Meta:
        verbose_name="tipo de menú"
        verbose_name_plural="tipos de menú"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return '../'

# Modelo de los Platos
class Plato(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    descripcion = models.TextField(max_length=400, verbose_name="Descripción")
    categoria = models.ForeignKey(Categoria, null=True, on_delete=models.SET_NULL, verbose_name="Categoría")
    precio = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Precio del plato") # una habitacón puede costar como máximo 999,99
    foto = models.ImageField(upload_to="fotos/platos/", verbose_name="Foto")
    tipo_menu = models.ManyToManyField(TipoMenu, verbose_name="Menu", related_name="get_menus")

    class Meta:
        verbose_name="plato"
        verbose_name_plural="platos"
        ordering = ['categoria', 'nombre']

    def __str__(self):
        return self.nombre + " " + str(self.precio) + " €"

    def get_absolute_url(self):
        return '../'
        