from django.shortcuts import render
from .models import Post
from django.utils import timezone

# Create your views here.
def index(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/index.html', {'posts': posts})

def intro(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/intro.html', {'posts': posts})

def about(request):
	return render(request, 'blog/about.html')

def q1(request):
	return render(request, 'blog/q1.html')

def q2(request):
	return render(request, 'blog/q2.html')

def q3(request):
	return render(request, 'blog/q3.html')

def q4(request):
	return render(request, 'blog/q4.html')

def conclusion(request):
	return render(request, 'blog/conclusion.html')