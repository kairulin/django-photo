from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title', 'build_time', 'update_time']
    list_filter = ['title','update_time']
    ordering = ['update_time']
