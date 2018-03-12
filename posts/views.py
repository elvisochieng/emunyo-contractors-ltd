from django.shortcuts import render
from .models import Post

def list_view(request):
	queryset = Post.objects.all()
	context = {'posts' : queryset}
	return render(request, 'post_list.html', context)

def detail_view(request, slug):
	queryset = Post.objects.get(slug=slug)
	context = {'detail':queryset}
	return render(request, 'post_detail.html', context)