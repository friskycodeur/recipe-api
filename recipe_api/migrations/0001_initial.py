# Generated by Django 3.2.3 on 2021-05-28 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('ingredients', models.TextField()),
                ('procedure', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('time_to_make', models.IntegerField(default=0)),
                ('tags', models.ManyToManyField(to='recipe_api.Tag')),
            ],
        ),
    ]
