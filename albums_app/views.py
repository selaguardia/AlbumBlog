from django.shortcuts import render
# View class to hangle requests
from django.views import View
# to hanfle sending a type of requests
from django.http import HttpResponse

# Create your views here.
class Home(View):
  def get(self, request):
    return HttpResponse('Albums Homepage')

class About(View):
  def get(self, request):
    return HttpResponse('Albums About page')