# Generated by Django 3.0.5 on 2020-06-04 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0020_auto_20200604_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.ImageField(blank=True, default='store.png', null=True, upload_to=''),
        ),
    ]