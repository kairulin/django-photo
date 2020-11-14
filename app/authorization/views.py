from . import models
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login as auth_login, logout
import random

# request = user.is_authenticated
# Create your views here.
def index(request):
    user_name = user_authenticated(request)  # 判斷是否有登入

    photo = models.Photo.objects.all()
    random_photo = random.sample(list(photo), k=5)
    result = {
        'random_photo': random_photo,
        'user_name': user_name
    }

    return render(request, 'index.html', result)


def post(request, pk):
    user_name = user_authenticated(request)  # 判斷是否有登入

    all_photo = models.Photo.objects.all()
    photo_path = all_photo.get(pk=pk)
    photo_exclude = list(all_photo.exclude(pk=pk))
    random.shuffle(photo_exclude)
    img = {
        'photo_path': photo_path.photo_file,
        'all_photo': photo_exclude,
        'user_name': user_name
    }

    return render(request, 'post.html', img)


def register(request):
    if request.method == 'POST':
        form = RegisterForm()
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect('/login/')
    else:
        form = RegisterForm()
    return render(request, 'register.html', locals())


def user_login(request):
    login_form = LoginForm()
    if request.method == "POST":
        user_name = request.POST.get("user_name")
        password = request.POST.get("password")
        user = authenticate(username=user_name, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('/')
    context = {
        'login_form': login_form
    }
    return render(request, 'login.html', context)


def user_logout(request):
    logout(request)
    return redirect('/')


def user_authenticated(request):
    if request.user.is_authenticated:
        user_name = request.user.username
    else:
        user_name = None
    return user_name
