# Generated by Django 5.0.7 on 2024-11-15 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0033_partecuerpo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partecuerpo',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
