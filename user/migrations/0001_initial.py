# Generated by Django 5.1.2 on 2024-11-04 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='car_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=25)),
                ('model', models.CharField(max_length=25)),
                ('price', models.CharField(max_length=25)),
            ],
        ),
    ]