from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Mmc
from mmc.models import Mmc
import math, json, re, random, simpy

# Create your views here.

class MMcQueue:
	def __init__(self, env, arrival_rate, service_rate, num_servers, packagesInQueue, queueEventTimes):
		self.env = env
		self.arrival_rate = arrival_rate
		self.service_rate = service_rate
		self.num_servers = num_servers
		self.queue = simpy.Store(env)
		self.servers = simpy.Resource(env, capacity=num_servers)
		self.waiting_times = []
		self.queue_lenght = 0
		self.packagesInQueue = packagesInQueue
		self.queueEventTimes = queueEventTimes

	def arrival_process(self):
		customer_id = 1

		for i in self.service_rate:
			inter_arrival_time = random.expovariate(self.arrival_rate)
			yield self.env.timeout(inter_arrival_time)
			self.queue_lenght += 1
			# print(f"Customer {customer_id} arrives at time {self.env.now}, packages in the queue: {self.queue_lenght}")
			self.env.process(self.service_process(customer_id, i))
			customer_id += 1
			self.packagesInQueue.append(self.queue_lenght)
			self.queueEventTimes.append(self.env.now)

	def service_process(self, customer_id, service):
		arrival_time = self.env.now
		
		with self.servers.request() as request:
			yield request
			service = float(service)

			service = service if service != 0.0 else 0.1

			service_time = random.expovariate(service)
			yield self.env.timeout(service_time)
			
			departure_time = self.env.now
			wait_time = departure_time - arrival_time
			self.waiting_times.append(wait_time)
			self.queue_lenght -= 1
			# print(f"Customer {customer_id} departs at time {departure_time} (Wait time: {wait_time}), packages in the queue: {self.queue_lenght}")
			self.packagesInQueue.append(self.queue_lenght)
			self.queueEventTimes.append(departure_time)


def run_simulation(arrival_rate, service_rate, num_servers, simulation_time, packagesInQueue, queueEventTimes):
	env = simpy.Environment()
	queue = MMcQueue(env, arrival_rate, service_rate, num_servers, packagesInQueue, queueEventTimes)
	env.process(queue.arrival_process())
	env.run(until=simulation_time)

	average_waiting_time = sum(queue.waiting_times) / len(queue.waiting_times)
	# print(f"Average Waiting Time: {average_waiting_time:.2f}")


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


		packagesInQueue = []
		queueEventTimes = [1]
	

		while len(queueEventTimes) % 2 != 0:
			packagesInQueue = []
			queueEventTimes = []
			run_simulation(myLambda, mu_k, c, 10.0, packagesInQueue, queueEventTimes)

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
		packagesInQueue = []
		queueEventTimes = []
		
	v = 1000

	if request.method == 'POST':
		myLambda = float(request.POST['myLambda'])
		mu = float(request.POST['mu'])
		c = int(request.POST['c'])

		if request.POST['v'] != '':
			v = int(request.POST['v'])

		rho = float("{:.3f}".format(myLambda/(c * mu)))

		if (c != 0) and (mu != 0) and (rho != 1) and (mu * c > myLambda):
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


			queueEventTimes = [1]

			while len(queueEventTimes) % 2 != 0:
				packagesInQueue = []
				queueEventTimes = []
				run_simulation(myLambda, mu_k, c, 10.0, packagesInQueue, queueEventTimes)

			newMmc = Mmc(myLambda = myLambda, mu = mu, c = c, rho = rho, k = k, mu_k = mu_k, p_0 = p_0, p_k = p_k, p_queue = p_queue, l_q = l_q, l_s = l_s,
				l_x = l_x, w_q = w_q, w_s = w_s, w_s_graph = w_s_graph, packagesInQueue= packagesInQueue, queueEventTimes = queueEventTimes)
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
		"w_s_graph": w_s_graph,
		"packagesInQueue": packagesInQueue,
		"queueEventTimes": queueEventTimes
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