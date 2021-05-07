from django.db import models
from django.core.validators import MinLengthValidator, MaxValueValidator


class Make(models.Model):
    name = models.CharField(max_length=128, validators=[MinLengthValidator(2, "Please enter a name with 2 or more characters")])

    def __str__(self):
        return self.name


class Auto(models.Model):
    nickname = models.CharField(max_length=128, validators=[MinLengthValidator(2, "Please enter a nickname with 2 or more characters")])
    make = models.ForeignKey('Make', on_delete=models.CASCADE, null=False)
    mileage = models.PositiveIntegerField(validators=[MaxValueValidator(999999, "Please enter a number less than 1000000")])
    comments = models.CharField(max_length=512)

    def __str__(self):
        return self.nickname
