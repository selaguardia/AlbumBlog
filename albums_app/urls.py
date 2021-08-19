from django.urls import path
from . import views
from .views import Home, About, AlbumCreate

urlpatterns = [
  path('', Home.as_view(), name='home'),
  path('about/', About.as_view(), name='about'),
  path('new/', AlbumCreate.as_view(), name='album_create'),
]