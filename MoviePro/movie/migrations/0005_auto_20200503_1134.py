# Generated by Django 3.0.5 on 2020-05-03 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_customer_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, default='default_profile.png', null=True, upload_to=''),
        ),
    ]
