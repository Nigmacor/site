from django.shortcuts import render
from .models import Orders, Tag

def home(request):
	orders = Orders.objects.all()
	return render(request, 'home/index.html', context={'orders': orders})

def order_detail(request, id):
	order = Orders.objects.get(id__exact=id)
	return render(request, 'home/order_detail.html', context={'order': order})

def tag_list(request):
	tags = Tag.objects.all()
	return render(request, 'home/tags_list.html', context={'tags': tags})