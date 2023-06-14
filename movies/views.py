from django.shortcuts import render
from .models import *

# Girdiğim profil resminin filimler ekranında gözükmesi için userdan ıd alıcaz
from user.models import *
# Create your views here.
def index(request):
    return render(request, 'index.html')

def movies(request, profilId, slug):
    # Girdiğim profil resminin filimler ekranında gözükmesi için userdan ıd alıcaz
    profil = Profile.objects.get(id = profilId, slug = slug)

    populer = Movie.objects.filter(kategori__isim = 'Popüler')
    gundem = Movie.objects.filter(kategori__isim = 'Gündemde')
    context = {
        'populer':populer,
        'gundem':gundem,
        'profil':profil
    }
    return render(request,'browse-index.html',context)