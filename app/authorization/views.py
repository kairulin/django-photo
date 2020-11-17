from . import models
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from .forms import RegisterForm, LoginForm, PhotoMessageForm
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
import random


# request = user.is_authenticated
# Create your views here.


def index(request):  # 首頁
    username = user_authenticated(request)  # 判斷是否有登入

    photo = models.Photo.objects.all()
    random_photo = random.sample(list(photo), k=8)  # 隨機抽圖片
    result = {
        'random_photo': random_photo,
        'username': username
    }

    return render(request, 'index.html', result)


def post(request, pk):  # 圖片頁面
    username = user_authenticated(request)  # 判斷是否有登入
    all_photo = models.Photo.objects.all()  # 所有的圖片
    wanna_photo = all_photo.get(pk=pk)  # 選擇的圖片
    photo_exclude = list(all_photo.exclude(pk=pk))  # 除了選擇的圖片 的其他圖片
    random.shuffle(photo_exclude)  # 其他圖片打亂位置

    img = {
        'photo_title': wanna_photo.title,  # 圖片標題
        'photo_path': wanna_photo.photo_file,  # 圖片連結
        'photo_likes': wanna_photo.photo_likes,  # 喜歡
        'photo_hates': wanna_photo.photo_hates,  # 討厭
        'photo_exclude': photo_exclude,  # 除了被選到的圖片以外的dict
        'username': username,
    }

    if 'ok' in request.GET:
        content = request.GET['content']
        models.PhotoMessage.objects.create(
            photo=wanna_photo,
            message_user=username,
            message_content=content
        )
        models.PhotoMessage.objects.update()

    return render(request, 'post.html', img)


def register(request):  # 註冊
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect('/login/')
            # if 'next' in request.GET:  # 留言後回到原本頁面
            #     return redirect(request.GET['next'])
    context = {
        'form': form
    }
    return render(request, 'register.html', context)


def user_login(request):  # 登入
    login_form = LoginForm()
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            # return redirect('/')
            if 'next' in request.GET:  # 登入後回到原本頁面
                return redirect(request.GET['next'])
            else:  # 如果是從非首頁位置註冊後導到登入頁面，則登入後導回首頁
                return redirect('/')
    context = {
        'login_form': login_form
    }
    return render(request, 'login.html', context)


def user_logout(request):  # 登出
    logout(request)
    # return redirect('/')
    if 'next' in request.GET:  # 登出後回到原本頁面
        return redirect(request.GET['next'])
    else:
        return redirect('/')


def user_authenticated(request):  # 判斷使用者是否有登入
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = None
    return username


def click_likes(request):
    get_list = get_photo(request)

    check_user_click(get_list[0], get_list[1], get_list[2])

    return redirect(request.GET['next'])


def click_hates(request):
    get_list = get_photo(request)

    check_user_click(get_list[0], get_list[1], get_list[2])

    return redirect(request.GET['next'])

def get_photo(request): #得到使用者、網址PK、使用者對這張圖片的感受 並放進list裡面
    username = user_authenticated(request)

    url_str = str(request)
    split_photo = url_str.strip('/').split('/')  # 分割網址
    photo_pk = split_photo[4] #抓這張圖的pk
    user_feel = split_photo[1] #使用者喜歡or不喜歡

    wanna_photo = models.Photo.objects.get(pk=photo_pk)

    get_list = [username, wanna_photo, user_feel]
    return get_list


def check_user_click(username, model, user_feel):  # 檢查這個使用者是否按過讚了
    try:
        if model.likes_hates_user.filter(username=username):
            print('你已經按過了')
        else:
            if user_feel == 'photo_likes':
                model.likes()
            elif user_feel == 'photo_hates':
                model.hates()
            model.likes_hates_user.add(User.objects.get(username=username))
    except Exception as e:
        print(e)
    return 0

# 下面是測試用
# def photo_message(request):  # 對圖片的留言
#     username = user_authenticated(request)  # 判斷是否有登入
#
#     if request.method == 'GET':
#         print('-' * 40)
#         message_form = PhotoMessageForm(request.POST)
#         message_form = message_form(initial={'message_user': 'this is test'})
#         print(message_form)
#         if message_form.is_valid():
#             print('yes')
#             message_form.save()
#             if 'next' in request.GET:  # 留言後回到原本頁面
#                 return redirect(request.GET['next'])
#     else:
#         message_form = PhotoMessageForm()
#     return render(request, 'test.html', locals())
