# Generated by Django 5.0.7 on 2024-10-24 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0023_causasproducenaccidente'),
    ]

    operations = [
        migrations.AddField(
            model_name='expediente',
            name='causas_accidente',
            field=models.TextField(blank=True, null=True),
        ),
    ]
