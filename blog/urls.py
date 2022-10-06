from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello, name='helo'),
    path('posts/', views.blog_all, name='posts'),
]
