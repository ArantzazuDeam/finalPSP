# Generated by Django 3.0.3 on 2020-02-18 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurante', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tipomenu',
            options={'ordering': ['nombre'], 'verbose_name': 'tipo de menú', 'verbose_name_plural': 'tipos de menú'},
        ),
    ]