from django.shortcuts import render
from .models import Post

def forum(request):
	posts = Post.objects.all()
	return render(request, 'forum/forum.html', context={'posts': posts})

def forum_detail(request, id):
	post = Post.objects.get(id__exact=id)
	return render(request, 'forum/forum_detail.html', context={'order': post})

def forum_list(request):
	
	return render(request, 'forum/forum_list.html')