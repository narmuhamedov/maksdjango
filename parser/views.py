from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import ListView, FormView
from . import parser, models, forms

class ParserView(ListView):
    model = models.ParserApp
    template_name = 'film_list.html'
    def get_queryset(self):
        return models.ParserApp.objects.all()


class ParserFormView(FormView):
    template_name = 'parser_film.html'
    form_class = forms.ParserForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return HttpResponse('<h1>Parsing Sucsessfuly</h1>')
        else:
            return super(ParserFormView, self).post(request, *args, **kwargs)


