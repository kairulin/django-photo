from django.shortcuts import render
from . import models, forms
from django.http import HttpResponse
# Create your views here.
def index(request):
    login_form = forms.LoginForm(request.POST)
    return render(request,'index.html',{'form':login_form})