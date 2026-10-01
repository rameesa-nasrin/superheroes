from django.db import models

# Create your models here.
class SuperHero(models.Model):

    name = models.CharField(max_length=100)

    real_name = models.CharField(max_length=100)

    age = models.IntegerField()

    power = models.CharField(max_length=100)

    origin = models.CharField(max_length=100)

    team = models.CharField(max_length=100)

    UNIVERSE_OPTIONS = [
        ("MARVEL","marvel"),
        ("DC","dc"),
        ("OTHER","other")
    ]

    universe = models.CharField(choices=UNIVERSE_OPTIONS,default="other")

def __str__(self):

    return self.name