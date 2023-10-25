from django.shortcuts import render
from .models import Mmc
from json import dumps

# Create your views here.
def home(request):
	c = 0
	myLambda = 0
	mu = 0
	mu_k = 0

	if request.method == 'POST':
		myLambda = float(request.POST['myLambda'])
		mu = float(request.POST['mu'])
		c = int(request.POST['c'])

		if myLambda == '' or mu == '' or c == '':
			myLambda = 0
			mu = 0
			c = 0
		
		newMmc = Mmc(myLambda = myLambda, mu = mu, c = c)
		newMmc.save()
		
		x = lambda k, c, mu : k * mu if (k * mu) < (c * mu) else c * mu
		mu_k = dumps([x(k, c, mu) for k in range(0, c + 10)])
		k = len([i for i in range(0, c + 10)]) - 1

	context = {
		"c": c,
		"mu_k": mu_k,
		"k": k
	}

	return render(request, 'mmc/index.html', context)