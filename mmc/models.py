from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Mmc(models.Model):
	myLambda = models.FloatField()
	mu = models.FloatField()
	c = models.FloatField()
	k = models.IntegerField()
	mu_k = ArrayField(models.FloatField())
	rho = models.FloatField()
	p_0 = models.FloatField()
	p_k = ArrayField(models.FloatField())
	p_queue = models.FloatField()
	l_q = models.FloatField()
	l_x = models.FloatField()
	l_s = models.FloatField()
	w_q = models.FloatField()
	w_s = models.FloatField()
	w_s_graph = ArrayField(models.FloatField())

	def __str__(self):
		return "Lambda: " + str(self.myLambda) + " Mu: " + str(self.mu) + " C: " + str(self.c)