# Generated by Django 5.0.7 on 2024-10-28 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0024_expediente_causas_accidente'),
    ]

    operations = [
        migrations.AddField(
            model_name='expediente',
            name='aplicar_accion',
            field=models.TextField(blank=True, null=True),
        ),
    ]
