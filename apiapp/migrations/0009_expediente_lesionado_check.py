# Generated by Django 5.0.7 on 2024-10-10 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0008_expediente_puesto_trabajo'),
    ]

    operations = [
        migrations.AddField(
            model_name='expediente',
            name='lesionado_check',
            field=models.BooleanField(default=False),
        ),
    ]