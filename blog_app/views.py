from django.shortcuts import render
from .models import Blog, Category, Tag
# Create your views here.


def home(request):
    #  blogs = Blog.objects.order_by('-created_at')
    blogs = Blog.objects.order_by('-created_date')[:3]
    categories = Category.objects.all()
    tags = Tag.objects.all()[:9]
    context = {
        'blogs': blogs,
        'categories': categories,
        'tags': tags,
    }
    return render(request, 'home.html', context)


def blogs(request):
    blogs = Blog.objects.order_by('-created_date')[:3]
    categories = Category.objects.all()
    tags = Tag.objects.all()[:9]
    context = {
        'blogs': blogs,
        'categories': categories,
        'tags': tags,
    }
    return render(request, 'blogs.html', context)


def blogDetails(request, pk):
    blogs = Blog.objects.order_by('-created_date')[:3]
    blog = Blog.objects.filter(pk=pk).first()
    categories = Category.objects.all()
    tags = Tag.objects.all()[:9]
    context = {
        'blog': blog,
        'blogs': blogs,
        'categories': categories,
        'tags': tags,
    }
    return render(request, 'post-details.html', context)
