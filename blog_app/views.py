from django.shortcuts import render
from .models import Blog, Category, Tag
from django.shortcuts import get_object_or_404
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


def categoryblogs(request, slug):
    category = get_object_or_404(Category, slug=slug)
    blogs = category.category_blogs.all()
    categories = Category.objects.all()
    tags = Tag.objects.all()[:9]
    context = {
        'blogs': blogs,
        'categories': categories,
        'tags': tags,
    }
    return render(request, 'category_blogs.html', context)


def tagBlogs(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    blogs = tag.tag_blogs.all()
    print("blog", blogs)
    categories = Category.objects.all()
    tags = Tag.objects.all()[:9]
    context = {
        'blogs': blogs,
        'categories': categories,
        'tags': tags,
    }
    return render(request, 'tag_blogs.html', context)
