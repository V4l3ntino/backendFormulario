# Generated by Django 5.0.7 on 2024-10-10 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0007_alter_expediente_id_alter_imagenes_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='expediente',
            name='puesto_trabajo',
            field=models.TextField(blank=True, null=True),
        ),
    ]