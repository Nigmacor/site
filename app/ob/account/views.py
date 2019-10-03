from django.shortcuts import render
from django.http import HttpResponse


def registration(request):
	return render(request, 'account/register.html')

def autorisation(request):
	return render(request, 'account/login.html')

def regphis(request):
	return render(request, 'account/phis.html')

def regjur(request):
	return render(request, 'account/jur.html')