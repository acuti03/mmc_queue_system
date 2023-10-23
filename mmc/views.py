from django.shortcuts import render
from .models import Mmc

# Create your views here.
def home(request):
	c = 0;

	if request.method == 'POST':
		myLambda = request.POST['myLambda']
		mu = request.POST['mu']
		c = request.POST['c']
	
		newMmc = Mmc(myLambda = myLambda, mu = mu, c = c)
		newMmc.save()

	c = int(c);
	context = { 
		"data" : [n for n in range(0,c)], 
	} 

	return render(request, 'mmc/index.html', context)