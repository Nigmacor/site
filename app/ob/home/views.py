from django.shortcuts import render
from .models import Orders

def home(request):
	orders = Orders.objects.all()
	return render(request, 'home/index.html', context={'orders': orders})
