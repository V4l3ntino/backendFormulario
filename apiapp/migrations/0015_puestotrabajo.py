# Generated by Django 5.0.7 on 2024-10-14 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0014_alter_imagenes_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='PuestoTrabajo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField()),
            ],
        ),
    ]
