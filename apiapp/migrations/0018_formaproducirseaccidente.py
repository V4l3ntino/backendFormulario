# Generated by Django 5.0.7 on 2024-10-16 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0017_lugaraccidente'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormaProducirseAccidente',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.TextField()),
            ],
        ),
    ]
