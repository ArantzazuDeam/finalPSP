from django.db import models

# Create your models here.
'''
class Persona(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)

    def __str__(self):
        return self.nombre+" "+self.apellido
'''

class Empresa(models.Model):
    nom=models.CharField(max_length=50, verbose_name="Nombre de la empresa")
    ciudad=models.CharField(max_length=50, verbose_name="Ciudad")

    def __str__(self):
        return self.nom
    
    class Meta:
        verbose_name="empresa"
        verbose_name_plural="empresas"
        ordering=["nom"]
        #ordering=["-nom"] # se ordenaría por el nombre de Z a A
    

class Empleado(models.Model):
    nombre=models.CharField(max_length=50, verbose_name="Nombre")
    apellido1=models.CharField(max_length=50, verbose_name="Primer apellido")
    apellido2=models.CharField(max_length=50, verbose_name="Segundo apellido")
    fecha_nac=models.DateField(auto_now_add=True, verbose_name="Fecha de nacimiento")
    foto=models.ImageField(upload_to='fotos/', verbose_name="Foto")
    emp=models.ForeignKey(Empresa, on_delete=models.DO_NOTHING, verbose_name="Empresa donde trabaja")

    def __str__(self):
        return self.nombre+" "+self.apellido1+" "+self.apellido2+" "+self.emp.nom
    
    class Meta:
        verbose_name="empleado"
        verbose_name_plural="empleados"
        ordering=["-fecha_nac"] # ordenados de más joven a más anciano