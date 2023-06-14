from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    # id ekleyeceğimiz için <profilId> kodu yazdık
    path('movies/<profilId>/<slug>',movies,name = 'movies')
]