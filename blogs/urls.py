from django.urls import path
from .import views


app_name = 'blogs'
urlpatterns = [
    path('', views.index, name='index'),
    path('detail_all', views.detail_all, name='detail_all'),
    path('detail/<int:blog_id>/', views.detail, name='detail'),
    path('detail/genre<int:genre_id>/', views.genre_detail, name='genre_detail'),
    path('price', views.price, name='price'),
    # path('contact', views.contact_index, name='contacttop'),  # 一覧画面
    path('contact_form/', views.contact_form, name='contact_form'),  # フォーム
    path('contact_form/contact/complete/', views.complete, name='complete'),  # 完了画面
]
