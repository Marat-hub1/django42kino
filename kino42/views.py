from msilib.schema import ListView

from django.shortcuts import render
from .models import *
import random
def index (request):
    films=Kino.objects.all()
    artists=Artist.objects.all()
    print(films)
    print(artists)
    randomFilm=random.choices(films)
    data={'randomFilm':randomFilm,'films':films, 'artists':artists}

    return render (request, 'index.html',data)

from django.views import generic
class kinolist(generic.ListView):
    model =Kino

class artistlist(generic.ListView):
    model =Artist

class KinoDetail(generic.DetailView):
    model=Kino

def num(request,num):
    print(num)
    return render(request,'index.html')

# Create your views here.
