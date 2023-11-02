from django.shortcuts import render
from .models import Mmc
from mmc.models import Mmc
import math, json, re

# Create your views here.
def cErlang(c, rho, p_0):
	return (p_0) * (((c * rho) ** c) / math.factorial(c)) * (1 / (1 - rho))

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
	v = 1000

	if request.method == 'POST':
		myLambda = float(request.POST['myLambda'])
		mu = float(request.POST['mu'])
		c = int(request.POST['c'])

		if request.POST['v'] != '':
			v = int(request.POST['v'])

		rho = float("{:.3f}".format(myLambda/(c * mu)))

		if c != 0 and mu != 0 and rho != 1:
			x = lambda a : a if a > 0 else -a

			myLambda = x(myLambda)
			mu = x(mu)
			c = x(c)

			x = lambda k, c, mu : "{:.3f}".format(k * mu) if (k * mu) < (c * mu) else "{:.3f}".format(c * mu)

			mu_k = ([x(k, c, mu) for k in range(0, c + 11)])
			k = len([i for i in range(0, c + 10)])

			for i in range(0, c):
				p_0 += ((c * rho) ** i) / math.factorial(i) + (((c * rho) ** c) / math.factorial(c)) * (1 / (1 - rho))
			p_0 = float("{:.3f}".format(p_0 ** -1))

			p_k = [i for i in range(0, k + 1)]
			for k in p_k:
				if k <= c:
					p_k[k] = float("{:.3f}".format(p_0 * ((c * rho) ** k) / math.factorial(k)))
				else:
					p_k[k] = float("{:.3f}".format(p_0 * ((rho ** k) * (c ** c)) / math.factorial(c)))

			p_queue = float("{:.3f}".format(cErlang(c, rho, p_0)))
			l_q = float("{:.3f}".format(cErlang(c, rho, p_0) * (rho / (1 - rho))))
			l_x = float("{:.3f}".format(c * rho))
			l_s = float("{:.3f}".format(l_q + l_x))
			w_q = float("{:.3f}".format(cErlang(c, rho, p_0) / ((c * mu) * (1 - rho))))
			w_s = float("{:.3f}".format((cErlang(c, rho, p_0) + (c * (1 - rho))) / ((c * mu) * (1 - rho))))

			newMmc = Mmc(myLambda = myLambda, mu = mu, c = c)
			newMmc.save()


	context = {
		"v": v,
		"myLambda": myLambda,
		"mu": mu,
		"c": c,
		"mu_k": json.dumps(mu_k),
		"k": k,
		"rho": rho,
		"p_0": p_0,
		"p_k": json.dumps(p_k),
		"p_queue": p_queue,
		"l_q": l_q,
		"l_x": l_x,
		"l_s": l_s,
		"w_q": w_q,
		"w_s": w_s
	}

	return render(request, 'mmc/index.html', context)

def grafici(request):
	#data = [i for i in Mmc.objects.values()]
	#myLambda = re.findall("\d+\.\d+", str([i for i in Mmc.objects.values("myLambda")]))
	#mu = re.findall("\d+\.\d+", str([i for i in Mmc.objects.values("mu")]))
	#c = re.findall("\d+\.\d+", str([i for i in Mmc.objects.values("c")]))
	myLambda = [float(i) for i in re.findall("\d+\.\d+", str([i for i in Mmc.objects.values("myLambda")]))]
	mu = [float(i) for i in re.findall("\d+\.\d+", str([i for i in Mmc.objects.values("mu")]))]
	c = [int(i) for i in [float(i) for i in re.findall("\d+\.\d+", str([i for i in Mmc.objects.values("c")]))]]

	print("lambda: ", myLambda)
	print("mu: ", mu)
	print("c:", c)

	context = {
		"myLambda": myLambda,
		"mu": mu,
		"c": c
	}
	return render(request, 'mmc/grafici.html', context)