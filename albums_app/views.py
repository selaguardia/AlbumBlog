from django.shortcuts import render
# View class to hangle requests
from django.views import View
# to hanfle sending a type of requests
# from django.http import HttpResponse
from django.views.generic.base import TemplateView

# Create your views here.
class Home(TemplateView):
  template_name = 'home.html'

class About(TemplateView):
  template_name = 'about.html'