# Generated by Django 3.1.4 on 2021-05-07 06:43

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Make',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, validators=[django.core.validators.MinLengthValidator(2, message='Please enter a name with 2 or more characters')])),
            ],
        ),
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=128, validators=[django.core.validators.MinLengthValidator(2, message='Please enter a nickname with 2 or more characters')])),
                ('mileage', models.IntegerField(validators=[django.core.validators.MinValueValidator(0, message='Please enter a positive number'), django.core.validators.MaxValueValidator(999999, message='Please enter a number less than 1000000')])),
                ('comments', models.CharField(max_length=512)),
                ('make', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autos.make')),
            ],
        ),
    ]