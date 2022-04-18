from django.shortcuts import render, HttpResponse, redirect
from .models import *
# Create your views here.

def index(request):
    kategori = ogr.objects.all()
    return render(request, "index.html",{"kategori":kategori})

def ornek(request):
     return render(request, "selam.html")

def urun_goster(request,id):
    ogr = bilgi.objects.filter(id = id)
    return render(request, "urun_goster.html", {"ogr":ogr})

def urun_tek_goster(request,id):
    obje = bilgi.objects.filter(kategori = id)
    ogr = bilgi.objects.all()[:3]
    return render(request, "tek_urun.html", {"ogr":ogr,"obj":obje})
"""
def dinamik(request,id):
    data = bilgi.objects.filter(id = id)
    sozluk = {"og":data}
    return render(request, "font.html", sozluk)
"""

