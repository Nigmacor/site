from django.shortcuts import render


def forum(request):
	
	return render(request, 'forum/forum.html')

def forum_detail(request):
	
	return render(request, 'forum/forum_detail.html')

def forum_list(request):
	
	return render(request, 'forum/forum_list.html')