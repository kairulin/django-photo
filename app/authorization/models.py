from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone


# Create your models here.
class Photo(models.Model):
    title = models.CharField(max_length=20)
    photo_file = models.ImageField(upload_to='static/images/')
    build_time = models.DateTimeField(auto_now=False)
    update_time = models.DateTimeField(auto_now=True)
    likes_hates_user = models.ManyToManyField(User)
    photo_likes = models.IntegerField(default=0)
    photo_hates = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.photo_file.delete()
        return super().delete(*args, **kwargs)

    def likes(self):
        self.photo_likes += 1
        self.save(update_fields=['photo_likes'])

    def hates(self):
        self.photo_hates += 1
        self.save(update_fields=['photo_hates'])


class PhotoMessage(models.Model):
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    message_user = models.CharField('使用者', max_length=20)
    message_content = models.TextField('留言', blank=True)
    message_create_date = models.DateTimeField('留言日期', null=False, auto_now_add=True)
    message_likes = models.IntegerField(default=0)
    message_hates = models.IntegerField(default=0)

    def __str__(self):
        return self.message_content

    class Meta:
        ordering = ('message_create_date',)

    def likes(self):
        self.message_likes += 1
        self.save(update_fields=['message_likes'])

    def hates(self):
        self.message_hates += 1
        self.save(update_fields=['message_hates'])
