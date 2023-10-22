from django.db import models

# Create your models here.
class Mmc(models.Model):
    myLambda = models.FloatField()
    mu = models.FloatField()
    c = models.IntegerField()

    def __str__(self):
        return "Lambda: " + str(self.myLambda) + " Mu: " + str(self.mu)