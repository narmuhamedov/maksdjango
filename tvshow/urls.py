from django.urls import path
from . import views

urlpatterns = [
    path('tvshows/', views.tvshow, name='tvshow'),
    path('tvshows/<int:id>/', views.tvshow_detail, name='detail'),
]
