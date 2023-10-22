from django.shortcuts import render
from .models import Mmc

# Create your views here.
def home(request):
    if request.method == 'POST':
        myLambda = request.POST['myLambda']
        mu = request.POST['mu']
        c = request.POST['c']

        newMmc = Mmc(myLambda = myLambda, mu = mu, c = c)
        newMmc.save()

    return render(request, 'mmc/index.html')