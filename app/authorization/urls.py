from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('',views.index),
    path('post/<int:pk>/',views.post),
    path('register/',views.register),
    path('login/',views.user_login),
    path('logout/',views.user_logout),
]