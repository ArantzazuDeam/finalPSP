# Generated by Django 3.0.3 on 2020-02-12 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.CharField(max_length=10, verbose_name='Dni')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('apellidos', models.CharField(max_length=150, verbose_name='Apellidos')),
                ('telefono', models.CharField(max_length=15, verbose_name='Teléfono')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'cliente',
                'verbose_name_plural': 'clientes',
                'ordering': ['apellidos', 'nombre'],
            },
        ),
        migrations.CreateModel(
            name='Habitacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20, unique=True, verbose_name='Nombre')),
                ('descripcion', models.TextField(max_length=400, verbose_name='Descripción')),
                ('precio_noche', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Precio por noche')),
                ('foto', models.ImageField(max_length=400, upload_to='fotos/habitaciones/', verbose_name='Imagen de la habitación')),
            ],
            options={
                'verbose_name': 'habitación',
                'verbose_name_plural': 'habitaciones',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=10, verbose_name='Tipo de pago')),
                ('descripcion', models.TextField(max_length=400, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'modo de pago',
                'verbose_name_plural': 'modos de pago',
                'ordering': ['tipo'],
            },
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField(verbose_name='Fecha de entrada')),
                ('fecha_fin', models.DateField(verbose_name='Fecha de salida')),
                ('num_personas', models.PositiveSmallIntegerField(verbose_name='Número de personas')),
                ('num_habitaciones', models.PositiveSmallIntegerField(verbose_name='Número de habitaciones')),
                ('precio_total', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Precio total')),
                ('pagado', models.BooleanField(default=False, verbose_name='Pagado')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.Cliente', verbose_name='Cliente')),
                ('modo_pago', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestion.Pago', verbose_name='Modo de pago')),
            ],
            options={
                'verbose_name': 'factura',
                'verbose_name_plural': 'facturas',
                'ordering': ['fecha_inicio'],
            },
        ),
        migrations.CreateModel(
            name='Detalle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_noches', models.PositiveIntegerField(verbose_name='Número de noches')),
                ('precio_hab_noches', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Precio de la habitación por num_noches')),
                ('habitacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.Habitacion', verbose_name='Habitación')),
                ('reserva', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.Factura', verbose_name='Factura')),
            ],
            options={
                'verbose_name': 'linea detallada de factura',
                'verbose_name_plural': 'linea detalladas de factura',
            },
        ),
    ]