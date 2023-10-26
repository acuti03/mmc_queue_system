from django.shortcuts import render
from .models import Mmc
from json import dumps
import math

# Create your views here.
def home(request):
	c = 0
	myLambda = 0
	mu = 0
	mu_k = 0
	k = 0
	rho = 0

	if request.method == 'POST':
		myLambda = float(request.POST['myLambda'])
		mu = float(request.POST['mu'])
		c = int(request.POST['c'])

		x = lambda a : a if a > 0 else (1 if a == 0 else -a)

		myLambda = x(myLambda)
		mu = x(mu)
		c = x(c)
		
		newMmc = Mmc(myLambda = myLambda, mu = mu, c = c)
		newMmc.save()
		
		x = lambda k, c, mu : "{:.2f}".format(k * mu) if (k * mu) < (c * mu) else "{:.2f}".format(c * mu)
		mu_k = dumps([x(k, c, mu) for k in range(0, c + 10)])
		k = len([i for i in range(0, c + 10)]) - 1
		rho = "{:.2f}".format(myLambda/(c * mu))

	context = {
		"c": c,
		"mu_k": mu_k,
		"k": k,
		"rho": rho
	}

	return render(request, 'mmc/index.html', context)