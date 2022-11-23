from django.urls import path
from . import views

app_name = 'blogs'
urlpatterns = [
    path('', views.index, name='index'),
    path('detail_all', views.detail_all, name='detail_all'),
    path('detail/<int:blog_id>/', views.detail, name='detail'),
    path('detail/genre<int:genre_id>/', views.genre_detail, name='genre_detail'),
]
