from django.db import models
from django.db.models import Model, CharField, DateField, TextField, DateTimeField

# Create your models here.
class Album(Model):
  title = CharField(max_length=150)
  artist = CharField(max_length=150)
  release_date = DateField()
  cover_img = CharField(max_length=500)
  description = TextField(max_length=500)
  created_at = DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title

  class Meta:
    ordering = ['-created_at']

 