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
    random_photo = random.sample(list(photo), k=8) #隨機抽圖片
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
        'photo_title': photo_path.title, #圖片標題
        'photo_path': photo_path.photo_file, #圖片連結
        'all_photo': photo_exclude, #除了被選到的圖片以外的dict
        'user_name': user_name #使用者
    }

    return render(request, 'post.html', img)


def register(request): #註冊
    if request.method == 'POST':
        form = RegisterForm()
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect('/login/')
    else:
        form = RegisterForm()
    return render(request, 'register.html', locals())


def user_login(request): #登入
    login_form = LoginForm()
    if request.method == "POST":
        user_name = request.POST.get("user_name")
        password = request.POST.get("password")
        user = authenticate(username=user_name, password=password)
        if user is not None:
            auth_login(request, user)
            # return redirect('/')
            if 'next' in request.GET:  #登入後回到原本頁面
                return redirect(request.GET['next'])
    context = {
        'login_form': login_form
    }
    return render(request, 'login.html', context)


def user_logout(request): #登出
    logout(request)
    # return redirect('/')
    if 'next' in request.GET:  # 登出後回到原本頁面
        return redirect(request.GET['next'])

def user_authenticated(request): #判斷使用者是否有登入
    if request.user.is_authenticated:
        user_name = request.user.username
    else:
        user_name = None
    return user_name
