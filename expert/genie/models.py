from django.db import models
from .libs.enums import *

# Create your models here.


class Actor(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    birth_year = models.IntegerField()
    gender = models.CharField(choices=Gender.choices(), default=Gender.Male, max_length=10)
    hair_color = models.CharField(choices=HairColor.choices(), default=HairColor.Blond, max_length=100)
    skin_color = models.CharField(choices=Ethnicity.choices(), default=Ethnicity.White, max_length=100)
    country = models.CharField(choices=Country.choices(), default=Country.USA, max_length=100)
    won_oscar = models.BooleanField(default=False)
    action_star = models.BooleanField(default=False)
    comedian = models.BooleanField(default=False)


    def __str__(self):
        return "{0} {1}".format(self.firstname, self.lastname)
