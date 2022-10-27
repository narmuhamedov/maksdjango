from django.urls import path
from . import views

urlpatterns = [
    path('', views.tvshow, name='tvshow'),
    path('tvshows/<int:id>/', views.tvshow_detail, name='detail'),
    path('tvshows/<int:id>/update/', views.show_update, name='update'),
    path('tvshows/<int:id>/delete/', views.show_delete, name='show delete'),
    path('add-shows/', views.addshows, name='addshows'),
    path('about_us/', views.about_us, name='about_us'),
]
