# Generated by Django 3.1.7 on 2021-03-15 16:59

from django.db import migrations, models
import myConcreteREST.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='myConcrete_Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lote', models.CharField(default=myConcreteREST.models.myConcrete_Data.lote_string, max_length=100)),
                ('empresa', models.CharField(blank=True, default='', max_length=200)),
                ('fecha', models.DateField(auto_now_add=True, null=True)),
                ('hora', models.TimeField(auto_now_add=True, null=True)),
                ('cantidad', models.FloatField(blank=True)),
                ('t_producción', models.TimeField(blank=True)),
                ('ruc', models.CharField(max_length=11)),
                ('cemento', models.FloatField()),
                ('agregado_1', models.FloatField()),
                ('agregado_2', models.FloatField()),
                ('agua', models.IntegerField()),
                ('aditivo_1', models.IntegerField()),
            ],
        ),
    ]
