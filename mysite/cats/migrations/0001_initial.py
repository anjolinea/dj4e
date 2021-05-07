# Generated by Django 3.1.4 on 2021-05-07 20:42

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, validators=[django.core.validators.MinLengthValidator(2, 'Please enter a name with 2 or more characters')])),
            ],
        ),
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=128, validators=[django.core.validators.MinLengthValidator(2, 'Please enter a nickname with 2 or more characters')])),
                ('weight', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(999, 'Please enter a number less than 1000')])),
                ('foods', models.CharField(max_length=300)),
                ('breed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cats.breed')),
            ],
        ),
    ]