# Generated by Django 5.0.7 on 2024-10-15 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0016_alter_puestotrabajo_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='LugarAccidente',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.TextField()),
            ],
        ),
    ]