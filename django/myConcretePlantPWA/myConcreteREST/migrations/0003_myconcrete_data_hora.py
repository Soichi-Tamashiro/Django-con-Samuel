# Generated by Django 3.1.7 on 2021-03-15 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myConcreteREST', '0002_auto_20210315_1036'),
    ]

    operations = [
        migrations.AddField(
            model_name='myconcrete_data',
            name='hora',
            field=models.TimeField(auto_now_add=True, null=True),
        ),
    ]
