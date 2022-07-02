#created by me !DEEPAK 

from django.contrib import admin
from django.urls import path, include
from blog import views

urlpatterns = [
    path('fifa', views.fifa, name='fifa'),
    path('postComment', views.postComment, name="postComment"),
    path('', views.blogHome, name='blogHome'), 
    path('<str:slug>', views.blogPost, name='blogPost'),
    
]
