from django.db import models

# Create your models here.
class Photo(models.Model):
    title = models.CharField(max_length=20)
    photo_file = models.ImageField(upload_to='static/images/')
    build_time = models.DateTimeField(auto_now=False)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title