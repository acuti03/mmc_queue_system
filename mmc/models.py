from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Mmc(models.Model):
    myLambda = models.FloatField()
    mu = models.FloatField()
    c = models.FloatField()

    def __str__(self):
        return "Lambda: " + str(self.myLambda) + " Mu: " + str(self.mu) + " C: " + str(self.c)