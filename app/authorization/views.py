from django.shortcuts import render
from . import models, forms
from django.http import HttpResponse
# Create your views here.
def index(request):
    photo = models.Photo.objects.all()
    return render(request,'index.html',locals())