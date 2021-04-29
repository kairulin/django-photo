from django.contrib import admin
from . import models
from .models import Photo, PhotoMessage,PhotoLikeHate
# Register your models here.

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('user', 'title', 'photo_likes', 'photo_hates', 'build_time', 'update_time')
    list_filter = ('title','update_time')
    ordering = ('update_time',)

# admin.site.register(models.PhotoMessage)
@admin.register(PhotoMessage)
class PhotoMessageAdmin(admin.ModelAdmin):
    search_fields = ('message_user',)
    list_display = ('message_user', 'photo', 'message_content', 'message_create_date')
    ordering = ('message_create_date',)

@admin.register(PhotoLikeHate)
class PhotoLikeHateAdmin(admin.ModelAdmin):
    search_fields = ('photo',)
    list_display = ('user','photo')
    ordering = ('-created',)

