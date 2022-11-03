from django.urls import path
from . import views

urlpatterns = [
    path('tvshows/', views.TvShowView.as_view(), name='tvshow'),
    path('tvshows/<int:id>/', views.TvShowDetailView.as_view(), name='detail'),
    path('tvshows/<int:id>/update/', views.TVShowUpdateView.as_view(), name='update'),
    path('tvshows/<int:id>/delete/', views.TvShowDeleteView.as_view(), name='show delete'),
    path('add-shows/', views.TvShowCreateView.as_view(), name='addshows'),
    path('about_us/', views.about_us, name='about_us'),
    path('contacts/', views.contact, name='contact'),
    path('sliders/', views.sliders, name='sliders'),
]
