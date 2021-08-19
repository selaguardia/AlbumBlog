from django.shortcuts import render
# View class to handle requests
from django.views import View
# to hanfle sending a type of requests
# from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView

from .models import Album

# Create your views here.
class Home(TemplateView):
  template_name = 'home.html'

  def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["albums"] = Album.objects.all()
        return context

class About(TemplateView):
  template_name = 'about.html'

# GET POST /album
class AlbumCreate(CreateView):
  model = Album
  fields = ['title', 'artist', 'release_date', 'cover_img', 'description']
  template_name = 'album_create.html'