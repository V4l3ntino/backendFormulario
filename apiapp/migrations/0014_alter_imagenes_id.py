# Generated by Django 5.0.7 on 2024-10-11 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0013_alter_imagenes_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagenes',
            name='id',
            field=models.CharField(max_length=37, primary_key=True, serialize=False),
        ),
    ]
