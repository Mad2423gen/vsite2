from django.shortcuts import render
from .models import Blog, Category


# Create your views here.
def index(request):
    blogs = Blog.objects.order_by('-created_datetime')
    return render(request, 'blogs/index.html', {'blogs': blogs})


def detail(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    return render(request, 'blogs/detail.html', {'blog': blog})


# def index(request):
#     blogs = Blog.objacts.order_by('-created_datetime')
#     return render(request, 'blogs/index.html', {'blogs': blogs})

def detail_all(request):
    blog_all = Blog.objects.order_by('-id')
    return render(request, 'blogs/detail_all.html', {'blog_all': blog_all})





