
from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render
from .models import Album

def index(request):
    all_albums = Album.objects.all()
   # template = loader.get_template("music/index.html")
    context = {'all_albums' : all_albums}
    return render(request, 'music/index.html', context) 

def detail(request, album_id):
    return HttpResponse('<h2>Details for album id : ' + album_id + '</h2>')

