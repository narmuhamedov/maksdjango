from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models, forms


#получение не полной информации о фильме
def tvshow(request):
    shows = models.TVShow.objects.all()
    return render(request, 'tvshows.html', {'shows_object': shows})


#получение id
def tvshow_detail(request, id):
    shows = get_object_or_404(models.TVShow, id=id)
    return render(request, 'tvshows_detail.html', {'shows_id':shows})


#create
def addshows(request):
    method = request.method
    if method == 'POST':
        form = forms.ShowForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Удачно добавлено')

    else:
        form = forms.ShowForm()

    return render(request, 'addtvshow.html', {'form': form})



#update
def show_update(request, id):
    show_object = get_object_or_404(models.TVShow, id=id)
    if request.method == "POST":
        form = forms.ShowForm(instance=show_object, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('TV good update')
    else:
        form = forms.ShowForm(instance=show_object)
    return render(request, 'tvshow_update.html', {'form': form, 'object': show_object})

#delete
def show_delete(request, id):
    show_object = get_object_or_404(models.TVShow, id=id)
    show_object.delete()
    return HttpResponse('Tv Show Deleted')

#Инфа о нас
def about_us(request):
    about = models.About_Us.objects.all()
    return render(request, "about.html", {'about':about})