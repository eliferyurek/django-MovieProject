# Generated by Django 3.0.5 on 2020-05-03 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0010_movie_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='actor',
            field=models.ManyToManyField(to='movie.Actor'),
        ),
    ]