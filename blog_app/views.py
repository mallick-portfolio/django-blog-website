from django.shortcuts import render
from .models import Blog
# Create your views here.


def home(request):
    #  blogs = Blog.objects.order_by('-created_at')
    blogs = Blog.objects.order_by('-created_date')[:3]
    context = {
        'blogs': blogs
    }
    return render(request, 'home.html', context)


def blogs(request):
    return render(request, 'blogs.html')
