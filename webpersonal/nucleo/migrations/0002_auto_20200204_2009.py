# Generated by Django 3.0.3 on 2020-02-04 20:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nucleo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='emp',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='nucleo.Empresa', verbose_name='Empresa donde trabaja'),
        ),
    ]
