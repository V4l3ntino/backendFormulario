# Generated by Django 5.0.7 on 2024-10-17 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0018_formaproducirseaccidente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trabajador',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
