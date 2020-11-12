from django.db import models

# Create your models here.
class ItemPhoto(models.Model):
    item_photo = models.ImageField()
