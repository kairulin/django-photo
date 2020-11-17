from django.urls import path


from . import views
urlpatterns = [
    path('',views.index),
    path('post/<int:pk>/',views.post),
    path('register/',views.register),
    path('login/',views.user_login),
    path('logout/',views.user_logout),
    path('photo_likes/',views.click_likes),
    path('photo_hates/',views.click_hates),
]