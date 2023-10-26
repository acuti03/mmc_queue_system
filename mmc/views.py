from django.shortcuts import render
from .models import Mmc
from json import dumps
import math

# Create your views here.
def home(request):
	c = 0
	myLambda = 0
	mu = 0
	mu_k = [0]
	k = [0]
	rho = 0
	p_0 = 0
	p_k = [0]

	if request.method == 'POST':
		myLambda = float(request.POST['myLambda'])
		mu = float(request.POST['mu'])
		c = int(request.POST['c'])

		x = lambda a : a if a > 0 else -a

		myLambda = x(myLambda)
		mu = x(mu)
		c = x(c)
		
		x = lambda k, c, mu : "{:.2f}".format(k * mu) if (k * mu) < (c * mu) else "{:.2f}".format(c * mu)

		mu_k = ([x(k, c, mu) for k in range(0, c + 10)])
		k = len([i for i in range(0, c + 10)]) - 1
		rho = float("{:.2f}".format(myLambda/(c * mu)))

		for i in range(0, c):
			p_0 += ((c * rho) ** i) / math.factorial(i) + (((c * rho) ** c) / math.factorial(c)) * (1/(1 - rho))
		p_0 = float("{:.2f}".format(p_0 ** -1))

		p_k = [i for i in range(0, k + 1)]
		for k in p_k:
			if k <= c:
				p_k[k] = float("{:.2f}".format(p_0 * ((c * rho) ** k) / math.factorial(k)))
			else:
				p_k[k] = float("{:.2f}".format(p_0 * ((rho ** k) * (c ** c)) / math.factorial(c)))


		print(k)
		newMmc = Mmc(myLambda = myLambda, mu = mu, c = c)
		newMmc.save()


	context = {
		"c": c,
		"mu_k": dumps(mu_k),
		"k": k,
		"rho": rho,
		"p_0": p_0,
		"p_k": dumps(p_k)
	}

	return render(request, 'mmc/index.html', context)