from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Mmc
from mmc.models import Mmc
import math, json, re

# Create your views here.
def cErlang(c, rho, p_0):
	return (p_0) * (((c * rho) ** c) / math.factorial(c)) * (1 / (1 - rho))

def selectFloat(string):
	return [float(i) for i in re.findall("\d+\.\d+", str([i for i in Mmc.objects.values(string)]))]

def selectInt(string):
	return [int(i) for i in re.findall("\d+", str([i for i in Mmc.objects.values(string)]))]


def home(request):
	tmp = selectFloat('myLambda')

	if tmp != []:
		myLambda = tmp
		myLambda = myLambda[len(myLambda) - 1]
		mu = selectFloat('mu')
		mu = mu[len(mu) - 1]
		c = selectInt('c')
		c = c[len(c) - 2]

		x = lambda k, c, mu : "{:.3f}".format(k * mu) if (k * mu) < (c * mu) else "{:.3f}".format(c * mu)

		mu_k = ([x(k, c, mu) for k in range(0, c + 11)])
		k = selectInt('k')
		k = k[len(k) - 1]
		rho = selectFloat('rho')
		rho = rho[len(rho) - 1]
		p_0 = selectFloat('p_0')
		p_0 = p_0[len(p_0) - 1]
		p_k = [i for i in range(0, k + 1)]

		for k in p_k:
			if k <= c:
				p_k[k] = float("{:.3f}".format(p_0 * ((c * rho) ** k) / math.factorial(k)))
			else:
				p_k[k] = float("{:.3f}".format(p_0 * ((rho ** k) * (c ** c)) / math.factorial(c)))

		p_queue = selectFloat('p_queue')
		p_queue = p_queue[len(p_queue) - 1]
		l_q = selectFloat('l_q')
		l_q = l_q[len(l_q) - 1]
		l_x = selectFloat('l_x')
		l_x = l_x[len(l_x) - 1]
		l_s = selectFloat('l_s')
		l_s = l_s[len(l_s) - 1]
		w_q = selectFloat('w_q')
		w_q = w_q[len(w_q) - 1]
		w_s = selectFloat('w_s')
		w_s = w_s[len(w_s) - 1]
		w_s_graph = [i for i in range(0, 99)]

		for i in w_s_graph:
			w_s_graph[i] = float("{:.3f}".format(((cErlang(c, i / 100, p_0) + (c * (1 - i / 100))) / ((c * mu) * (1 - i / 100))) * (mu * c)))

	else:
		myLambda = 0
		mu = 0
		c = 0
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
		w_s_graph = [0]
		
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
			w_s_graph = [i for i in range(0, 99)]

			for i in w_s_graph:
				w_s_graph[i] = float("{:.3f}".format(((cErlang(c, i / 100, p_0) + (c * (1 - i / 100))) / ((c * mu) * (1 - i / 100))) * (mu * c)))

			newMmc = Mmc(myLambda = myLambda, mu = mu, c = c, rho = rho, k = k, mu_k = mu_k, p_0 = p_0, p_k = p_k, p_queue = p_queue, l_q = l_q, l_s = l_s, l_x = l_x, w_q = w_q, w_s = w_s, w_s_graph = w_s_graph)
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
		"w_s": w_s,
		"w_s_graph": w_s_graph 
	}

	return render(request, 'mmc/index.html', context)

def grafici(request):
	data = Mmc.objects.all().values()

	context = {
		'data': data,
	}

	return render(request, 'mmc/grafici.html', context)

def delete(request, id):
	mmc = Mmc.objects.get(id=id)
	mmc.delete()

	return HttpResponseRedirect(reverse('grafici'))