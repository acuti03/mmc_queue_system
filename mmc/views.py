from django.shortcuts import render
from .models import Mmc
from json import dumps

# Create your views here.
def home(request):
	c = 0;
	myLambda = 0;
	mu = 0;

	if request.method == 'POST':
		myLambda = request.POST['myLambda']
		mu = request.POST['mu']
		c = request.POST['c']

		if myLambda == '' or mu == '' or c == '':
			myLambda = 0
			mu = 0
			c = 0
		
		newMmc = Mmc(myLambda = myLambda, mu = mu, c = c)
		newMmc.save()

	context = {
		"c": c,
	}

	return render(request, 'mmc/index.html', context)