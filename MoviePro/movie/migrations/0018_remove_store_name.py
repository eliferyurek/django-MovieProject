# Generated by Django 3.0.5 on 2020-05-29 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0017_city_store'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='name',
        ),
    ]
