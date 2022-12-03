# ブログ部分のつくりかた
# https://djangobrothers.com/tutorials/blog_app/introduction/
# カテゴリ一覧の書き方
# https://blog.narito.ninja/detail/150#_5
# https://blog.narito.ninja/detail/170
# moelについての解説
# https://qiita.com/kotayanagi/items/3cfadae951c407ac044a

from django.shortcuts import render
from .models import Blog, Category


# Create your views here.
def index(request):
    blogs = Blog.objects.order_by('-created_datetime')
    return render(request, 'blogs/index.html', {'blogs': blogs})


# ブログ部=============================================================================
def detail(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    return render(request, 'blogs/detail.html', {'blog': blog})


# ブログ記事総一覧
def detail_all(request):
    blog_all = Blog.objects.order_by('-id')
    return render(request, 'blogs/detail_all.html', {'blog_all': blog_all})


def genre_detail(request, genre_id):  # 親(Category)から逆参照してジャンル一覧を表示
    genre_details_obj = Category.objects.get(id=genre_id)
    return render(request, 'blogs/genre_detail_all.html',
                  {'genre_details_obj': genre_details_obj})


# ===================================================================================
# 価格表
def price(request):
    return render(request, 'blogs/price.html')
