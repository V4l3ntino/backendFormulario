# Generated by Django 5.0.7 on 2024-10-07 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0005_imagenes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expediente',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
