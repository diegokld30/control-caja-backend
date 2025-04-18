# Generated by Django 5.1.7 on 2025-03-16 03:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cajaDiaria', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleCaja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('tipo', models.CharField(choices=[('ingreso', 'Ingreso'), ('egreso', 'Egreso'), ('venta', 'Venta')], max_length=50)),
                ('monto', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('caja_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cajaDiaria.cajadiaria')),
            ],
        ),
    ]
