from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.views import generic


#получение не полной информации о фильме
class TvShowView(generic.ListView):
    template_name = 'tvshows.html'
    queryset = models.TVShow.objects.all()

    def get_queryset(self):
        return models.TVShow.objects.all()

# def tvshow(request):
#     shows = models.TVShow.objects.all()
#     return render(request, 'tvshows.html', {'shows_object': shows})


#получение id
class TvShowDetailView(generic.DetailView):
    template_name = 'tvshows_detail.html'

    def get_object(self, **kwargs):
        shows_id = self.kwargs.get('id')
        return get_object_or_404(models.TVShow, id=shows_id)
# def tvshow_detail(request, id):
#     shows = get_object_or_404(models.TVShow, id=id)
#     return render(request, 'tvshows_detail.html', {'shows_id':shows})


#create
class TvShowCreateView(generic.CreateView):
    template_name = 'addtvshow.html'
    form_class = forms.ShowForm
    queryset = models.TVShow.objects.all()
    success_url = "/tvshows/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(TvShowCreateView, self).form_valid(form=form)


# def addshows(request):
#     method = request.method
#     if method == 'POST':
#         form = forms.ShowForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Удачно добавлено')
#
#     else:
#         form = forms.ShowForm()
#
#     return render(request, 'addtvshow.html', {'form': form})



#update

class TVShowUpdateView(generic.UpdateView):
    template_name = 'tvshow_update.html'
    form_class = forms.ShowForm
    success_url = '/tvshows/'

    def get_object(self, **kwargs):
        show_id = self.kwargs.get('id')
        return get_object_or_404(models.TVShow, id=show_id)

    def form_valid(self, form):
        return super(TVShowUpdateView, self).form_valid(form=form)


# def show_update(request, id):
#     show_object = get_object_or_404(models.TVShow, id=id)
#     if request.method == "POST":
#         form = forms.ShowForm(instance=show_object, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('TV good update')
#     else:
#         form = forms.ShowForm(instance=show_object)
#     return render(request, 'tvshow_update.html', {'form': form, 'object': show_object})

#delete

class TvShowDeleteView(generic.DeleteView):
    template_name = 'confirm_delete.html'
    success_url = '/tvshows/'

    def get_object(self, **kwargs):
        show_id = self.kwargs.get('id')
        return get_object_or_404(models.TVShow, id=show_id)

# def show_delete(request, id):
#     show_object = get_object_or_404(models.TVShow, id=id)
#     show_object.delete()
#     return HttpResponse('Tv Show Deleted')

#Инфа о нас
def about_us(request):
    about = models.About_Us.objects.all()
    return render(request, "about.html", {'about':about})

#Инфа о контактах
def contact(request):
    contacts = models.Contact.objects.all()
    return render(request, 'contacts.html', {'contacts': contacts})

#Информация о сладайдах
def sliders(request):
    slide = models.Sliders.objects.all()
    return render(request, 'sliders.html', {'slide':slide})