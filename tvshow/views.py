from django.shortcuts import render, get_object_or_404
from . import models


#получение не полной информации о фильме
def tvshow(request):
    shows = models.TVShow.objects.all()
    return render(request, 'tvshows.html', {'shows_object': shows})


#получение id
def tvshow_detail(request, id):
    shows = get_object_or_404(models.TVShow, id=id)
    return render(request, 'tvshows_detail.html', {'shows_id':shows})