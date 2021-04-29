from rest_framework.routers import DefaultRouter

from app.authorization import views as authorization_views

router = DefaultRouter()

router.register('photo',authorization_views.PhotoViewSet)