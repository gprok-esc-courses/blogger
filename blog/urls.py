from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('blogpost/<str:slug>', views.blogpost),
    path('blog/<str:username>', views.blog),
    path('blog/add/post/', views.add_post),
    path('user', views.user),
    path('', views.index),
]