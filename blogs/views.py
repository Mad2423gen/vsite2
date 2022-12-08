# ブログ部分のつくりかた
# https://djangobrothers.com/tutorials/blog_app/introduction/
# カテゴリ一覧の書き方
# https://blog.narito.ninja/detail/150#_5
# https://blog.narito.ninja/detail/170
# moelについての解説
# https://qiita.com/kotayanagi/items/3cfadae951c407ac044a

from django.shortcuts import render, redirect
from .models import Blog, Category
from .forms import ContactForm
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import BadHeaderError, send_mail


# Create your views here.
def index(request):
    blogs = Blog.objects.order_by('-created_datetime')
    return render(request, 'blogs/index.html', {'blogs': blogs})


# ===================================================================================
# ブログ
def detail(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    return render(request, 'blogs/detail.html', {'blog': blog})


# ブログ記事総一覧
def detail_all(request):
    blog_all = Blog.objects.order_by('-id')
    return render(request, 'blogs/detail_all.html', {'blog_all': blog_all})


# 親(Category)から逆参照してジャンル一覧を表示
def genre_detail(request, genre_id):
    genre_details_obj = Category.objects.get(id=genre_id)
    return render(request, 'blogs/genre_detail_all.html',
                  {'genre_details_obj': genre_details_obj})


# ===================================================================================
# 価格表
def price(request):
    return render(request, 'blogs/price.html')


# ===================================================================================
# 問い合わせフォーム

""" 一覧画面"""


def contact_index(request):
    return render(request, 'contact/contactformtop.html')


""" お問い合わせフォーム画面"""


def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            myself = form.cleaned_data['myself']
            recipients = [settings.EMAIL_HOST_USER]

            if myself:
                recipients.append(sender)
            try:
                send_mail(subject, message, sender, recipients)
            except BadHeaderError:
                return HttpResponse('無効なヘッダーが見つかりました。')
            return redirect('blogs:complete')

    else:
        form = ContactForm()

    return render(request, 'contact/contact_form.html', {'form': form})


""" 送信完了画面"""


def complete(request):
    return render(request, 'contact/contactcomplete.html')
