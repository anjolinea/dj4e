from django.db import models
from django.core.validators import MinLengthValidator, MaxValueValidator, URLValidator

class Breed(models.Model):
    name = models.CharField(
            max_length=128,
            validators=[MinLengthValidator(2, "Please enter a name with 2 or more characters")]
    )

    def __str__(self):
        return self.name

class Cat(models.Model):
    nickname = models.CharField(
            max_length=128,
            validators=[MinLengthValidator(2, "Please enter a nickname with 2 or more characters")]
    )
    weight = models.PositiveIntegerField(validators=[MaxValueValidator(9999, "Please enter a number less than 10000")])
    foods = models.CharField(max_length=300)
    breed = models.ForeignKey('Breed', on_delete=models.CASCADE, null=False)
    image = models.URLField(max_length = 200, null=True,
                            validators=[URLValidator(regex="(.*imgur.*)", message="Please enter a link from imgur")])

    def __str__(self):
        return self.nickname
