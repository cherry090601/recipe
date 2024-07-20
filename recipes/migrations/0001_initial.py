# Generated by Django 5.0.7 on 2024-07-20 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=50)),
                ('preparation_time', models.IntegerField()),
                ('ingredients', models.TextField()),
                ('steps', models.TextField()),
            ],
        ),
    ]
