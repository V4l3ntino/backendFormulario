# Generated by Django 5.0.7 on 2024-11-15 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0037_expediente_agente_expediente_forma_producirse_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expediente',
            name='tipo_lesion',
        ),
    ]
