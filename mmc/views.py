from django.shortcuts import render
from .models import Mmc
from json import dumps
import math

# Create your views here.
def cErlang(a, c, p_0):
	return (((a ** c) / math.factorial(c)) * 1 / (1 - (a / c)) ) / p_0


def home(request):
	c = 0
	myLambda = 0
	mu = 0
	mu_k = [0]
	k = 0
	rho = 0
	p_0 = 0
	p_k = [0]
	p_queue = 0
	l_q = 0
	l_x = 0
	l_s = 0
	w_q = 0
	w_s = 0

	if request.method == 'POST':
		myLambda = float(request.POST['myLambda'])
		mu = float(request.POST['mu'])
		c = int(request.POST['c'])

		newMmc = Mmc(myLambda = myLambda, mu = mu, c = c)
		newMmc.save()

		if c is not 0 and mu is not 0:
			x = lambda a : a if a > 0 else -a

			myLambda = x(myLambda)
			mu = x(mu)
			c = x(c)

			x = lambda k, c, mu : "{:.3f}".format(k * mu) if (k * mu) < (c * mu) else "{:.3f}".format(c * mu)

			mu_k = ([x(k, c, mu) for k in range(0, c + 11)])
			k = len([i for i in range(0, c + 10)])
			rho = float("{:.3f}".format(myLambda/(c * mu)))

			if rho is 1:
				for i in range(0, c):
					p_0 += ((c * rho) ** i) / math.factorial(i) + (((c * rho) ** c) / math.factorial(c)) * (1 / (1 - rho))
				p_0 = float("{:.3f}".format(p_0 ** -1))

			p_k = [i for i in range(0, k + 1)]
			for k in p_k:
				if k <= c:
					p_k[k] = float("{:.3f}".format(p_0 * ((c * rho) ** k) / math.factorial(k)))
				else:
					p_k[k] = float("{:.3f}".format(p_0 * ((rho ** k) * (c ** c)) / math.factorial(c)))

			if p_0 is not 0:
				p_queue = float("{:.3f}".format(cErlang(rho * c, c, (p_0 ** -1))))
				l_q = float("{:.3f}".format(cErlang(rho * c, c, (p_0 ** -1)) * (rho / (1 - rho))))
				l_x = float("{:.3f}".format(c * rho))
				l_s = float("{:.3f}".format(l_q + l_x))
				w_q = float("{:.3f}".format(cErlang(rho * c, c, (p_0 ** -1)) / ((c * mu) * (1 - rho))))
				w_s = float("{:.3f}".format((cErlang(rho * c, c, (p_0 ** -1)) + (c * (1 - rho))) / ((c * mu)*(1 - rho))))

			print(p_queue)

	context = {
		"c": c,
		"mu_k": dumps(mu_k),
		"k": k,
		"rho": rho,
		"p_0": p_0,
		"p_k": dumps(p_k),
		"p_queue": p_queue,
		"l_q": l_q,
		"l_x": l_x,
		"l_s": l_s,
		"w_q": w_q,
		"w_s": w_s
	}

	return render(request, 'mmc/index.html', context)